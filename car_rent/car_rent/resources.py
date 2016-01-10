# coding: utf-8
import logging
import requests

from django.core.paginator import Paginator

from restless.dj import DjangoResource
from restless.exceptions import NotFound, Unauthorized
from restless.preparers import FieldsPreparer
from restless.resources import skip_prepare

from models import Token, Type, \
    Brand, Transport, City, Map
from tasks import create_map
from utils import API_URL_DIRECTIONS, GOOGLE_MAPS_API_KEY

logger = logging.getLogger('walmart_log.walmart_log.resources')


class BaseResource(DjangoResource):
    DEFAULT_PAGINATOR = 10

    dict_filters = {}

    preparer = FieldsPreparer(fields={})

    def not_found(self, class_name, field_type, id_data):
        raise NotFound(
            msg="404 - {0} with {1} {2} not found".format(
                class_name, field_type, id_data))

    def filters(self, request):
        items = {}
        for key, value in self.request.GET.items():
            if key in self.dict_filters:
                items[self.dict_filters.get(key)] = value
        return items

    def is_authenticated(self):
        try:
            self.token = Token.objects.get(token=self.request.GET.get('token'))
            return True
        except Token.DoesNotExist:
            raise Unauthorized(
                msg="Token {0} unauthorized or inexistent".format(
                    self.request.GET.get('token')))

    def serialize_list(self, data):
        data = self.paginate(data)
        self.meta = data.get('meta')
        return super(BaseResource, self).serialize_list(data.get('objects'))

    def wrap_list_response(self, data):
        return {
            'meta': self.meta,
            'objects': data,
        }

    def paginate(self, queryset):
        data = dict()

        limit = int(self.request.GET.get('limit', self.DEFAULT_PAGINATOR))
        self.paginator = Paginator(queryset, limit)
        self.page = int(self.request.GET.get('page', 1))

        meta = {
            'limit': limit,
            'next': self.paginator.page(self.page).has_next(),
            'previous': self.paginator.page(self.page).has_previous(),
            'total_count': self.paginator.count,
            'page': self.page,
        }

        data['meta'] = meta
        data['objects'] = self.paginator.page(self.page).object_list
        return data

    def get_google_info(self, origin, destination, waypoints):
        try:
            response = requests.get(
                API_URL_DIRECTIONS +
                'origin={0}&destination={1}&key={2}&waypoints=optimize:true|{3}'.format(
                    origin, destination, GOOGLE_MAPS_API_KEY,
                    waypoints), timeout=5).json()
            return self.prepare_route_data_info(response).value
        except:
            return False

    @skip_prepare
    def prepare_route_data_info(self, google_info):
        waypoint_order = google_info.get('routes')[0].get('waypoint_order')

        origin = self.request.GET.get('origin')
        destination = self.request.GET.get('destination')
        waypoint_list = []
        logistic_order = []
        try:
            waypoint_list = self.request.GET.get('waypoints').split("|")
            logistic_order = [waypoint_list[i] for i in waypoint_order]
        except:
            pass
        logistic_order.insert(0, origin)
        logistic_order.insert(len(waypoint_order)+1, destination)

        info = google_info.get('routes')[0].get('legs')
        list_info = []
        for i in info:
            info_route = {
                'distance': i.get('distance').get('value'),
                'start_address': i.get('start_address'),
                'end_address': i.get('end_address'),
            }
            list_info.append(info_route)

        sum_distance = sum([i.get('distance') for i in list_info])

        route_data = {
            'logistic_order': logistic_order,
            'name': self.request.GET.get('name'),
            'transport_sign': self.request.GET.get('transport_sign'),
            'city_origin': list_info[0].get('start_address'),
            'city_destiny': list_info[-1].get('end_address'),
            'total_distance': sum_distance / 1000,
            'gas_value': self.request.GET.get('gas_value'),
        }
        create_map.delay(route_data)
        return route_data

    def prepare(self, data):
        prepped = super(BaseResource, self).prepare(data)
        try:
            date_added = prepped['date_added']
            format_date = '%Y-%m-%d %H:%M:%S'
            prepped['date_added'] = date_added.strftime(format_date)
        except:
            pass
        return prepped


class TypeResource(BaseResource):
    fields = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Type.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.fields
        try:
            return self.queryset(request=self.request).get(id=pk)
        except Type.DoesNotExist:
            return self.not_found(self.__class__.__name__, "ID", pk)

    def create(self):
        return Type.objects.create(
            name=self.data['name'],
        )

    def update(self, pk):
        try:
            up_type = self.queryset(request=self.request).get(id=pk)
        except Type.DoesNotExist:
            return self.not_found(self.__class__.__name__, "ID", pk)
        up_type.name = self.data['name']
        up_type.slug = self.data['slug']
        up_type.save()
        return up_type

    def delete(self, pk):
        return Type.objects.get(id=pk).delete()


class BrandResource(BaseResource):
    fields = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Brand.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.fields
        try:
            return self.queryset(request=self.request).get(id=pk)
        except:
            return self.not_found(self.__class__.__name__, "ID", pk)

    def create(self):
        return Brand.objects.create(
            name=self.data['name'],
        )

    def update(self, pk):
        try:
            brand = self.queryset(request=self.request).get(id=pk)
        except Brand.DoesNotExist:
            return self.not_found(self.__class__.__name__, "ID", pk)
        brand.name = self.data['name']
        brand.slug = self.data['slug']
        brand.save()
        return brand

    def delete(self, pk):
        return Brand.objects.get(id=pk).delete()


class TransportResource(BaseResource):
    preparer_list = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    preparer_detail = {
        'id': 'id',
        'transport_way': 'transport_way',
        'transport_type': 'transport_type.slug',
        'brand': 'brand.slug',
        'name': 'name',
        'slug': 'slug',
        'sign': 'sign',
        'autonomy': 'autonomy',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Transport.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.preparer_list
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.preparer_detail
        try:
            return self.queryset(request=self.request).get(id=pk)
        except:
            return self.not_found(self.__class__.__name__, "ID", pk)

    def create(self):
        return Transport.objects.create(
            transport_way=self.data['transport_way'],
            transport_type=Type.objects.get(slug=self.data['transport_type']),
            brand=Brand.objects.get(slug=self.data['brand']),
            name=self.data['name'],
            sign=self.data['sign'],
            autonomy=self.data['autonomy'],
        )

    def update(self, pk):
        try:
            transport = Transport.objects.get(id=pk)
        except Transport.DoesNotExist:
            return self.not_found(self.__class__.__name__, "ID", pk)
        transport.transport_way = self.data['transport_way']
        transport.transport_type = Type.objects.get(
            slug=self.data['transport_type'])
        transport.brand = Brand.objects.get(slug=self.data['brand'])
        transport.name = self.data['name']
        transport.slug = self.data['slug']
        transport.sign = self.data['sign']
        transport.autonomy = self.data['autonomy']
        transport.save()
        return transport

    def delete(self, pk):
        return Transport.objects.get(id=pk).delete()


class CityResource(BaseResource):
    fields = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = City.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.fields
        try:
            return self.queryset(request=self.request).get(id=pk)
        except:
            return self.not_found(self.__class__.__name__, "ID", pk)


class MapResource(BaseResource):
    preparer_list = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'transport': 'transport.sign',
    }

    preparer_detail = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'transport': 'transport.sign',
        'city_origin': 'city_origin.name',
        'city_destiny': 'city_destiny.name',
        'logistic_order': 'logistic_order',
        'total_distance': 'total_distance',
        'gas_value': 'gas_value',
        'cost_percent': 'cost_percent',
        'date_added': 'date_added',
        'is_active': 'is_active',
    }

    def __init__(self, *args, **kwargs):
        super(MapResource, self).__init__(*args, **kwargs)
        self.http_methods.update({
            'get_map': {
                'GET': 'get_map'
            }
        })

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Map.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.preparer_list
        return self.queryset(request=self.request)

    def detail(self, slug):
        self.preparer.fields = self.preparer_detail
        try:
            return self.queryset(request=self.request).get(slug=slug)
        except:
            return self.not_found(self.__class__.__name__, "SLUG", slug)

    def get_map(self, *args, **kwargs):
        origin = self.request.GET.get('origin')
        destination = self.request.GET.get('destination')
        waypoints = self.request.GET.get('waypoints') or ""
        return self.get_google_info(origin, destination, waypoints)

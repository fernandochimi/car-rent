# coding: utf-8
import logging
# import requests

from datetime import datetime

from django.core.paginator import Paginator

from restless.dj import DjangoResource
from restless.exceptions import NotFound, Unauthorized
from restless.preparers import FieldsPreparer

from models import Token, Customer, \
    Vehicle, Rent
from utils import FORMAT_DATE

logger = logging.getLogger('car_rent.car_rent.resources')


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

    def prepare(self, data):
        prepped = super(BaseResource, self).prepare(data)
        try:
            date_added = prepped['date_added']
            date_checkout = prepped['date_checkout']
            date_checkin = prepped['date_checkin']
            prepped['date_added'] = datetime.strptime(date_added, FORMAT_DATE)
            prepped['date_checkout'] = datetime.strptime(
                date_checkout, FORMAT_DATE)
            prepped['date_checkin'] = datetime.strptime(
                date_checkin, FORMAT_DATE)
        except:
            pass
        return prepped


class CustomerResource(BaseResource):
    fields = {
        'id': 'id',
        'cnh': 'cnh',
        'name': 'name',
        'cpf': 'cpf',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Customer.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.fields
        try:
            return self.queryset(request=self.request).get(id=pk)
        except Customer.DoesNotExist:
            return self.not_found(self.__class__.__name__, "ID", pk)

    def create(self):
        self.preparer.fields = self.fields
        return Customer.objects.create(
            cnh=self.data['cnh'],
            name=self.data['name'],
            cpf=self.data['cpf'],
        )

    def update(self, pk):
        self.preparer.fields = self.fields
        try:
            up_customer = self.queryset(request=self.request).get(id=pk)
        except Customer.DoesNotExist:
            return self.not_found(self.__class__.__name__, "ID", pk)
        up_customer.chn = self.data['cnh']
        up_customer.chn = self.data['name']
        up_customer.save()
        return up_customer

    def delete(self, pk):
        return Customer.objects.get(id=pk).delete()


class VehicleResource(BaseResource):
    fields = {
        'id': 'id',
        'vehicle_category': 'vehicle_category',
        'name': 'name',
        'slug': 'slug',
        'sign': 'sign',
        'date_added': 'date_added',
        'is_avaliable': 'is_avaliable',
        'is_active': 'is_active',
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Vehicle.objects.all()
        return qs.filter(**filters)

    def list(self):
        self.preparer.fields = self.fields
        return self.queryset(request=self.request)

    def detail(self, pk):
        self.preparer.fields = self.fields
        try:
            print dir(self.queryset(request=self.request).get(id=pk))
            return self.queryset(request=self.request).get(id=pk)
        except:
            return self.not_found(self.__class__.__name__, "ID", pk)

    def create(self):
        self.preparer.fields = self.fields
        return Vehicle.objects.create(
            vehicle_category=self.data['vehicle_category'],
            name=self.data['name'],
            sign=self.data['sign'],
        )

    def update(self, pk):
        self.preparer.fields = self.fields
        try:
            up_vehicle = self.queryset(request=self.request).get(id=pk)
        except Vehicle.DoesNotExist:
            return self.not_found(self.__class__.__name__, "ID", pk)
        up_vehicle.vehicle_category = self.data['vehicle_category']
        up_vehicle.name = self.data['name']
        up_vehicle.slug = self.data['slug']
        up_vehicle.sign = self.data['sign']
        up_vehicle.is_avaliable = self.data['is_avaliable']
        up_vehicle.is_active = self.data['is_active']
        up_vehicle.save()
        return up_vehicle

    def delete(self, pk):
        return Vehicle.objects.get(id=pk).delete()


class RentResource(BaseResource):
    fields = {
        'id': 'id',
        'customer': 'customer.cpf',
        'vehicle': 'vehicle.slug',
        'mileage': 'mileage',
        'date_checkout': 'date_checkout',
        'date_checkin': 'date_checkin',
    }

    error_fields = {
        'msg': 'This car is not avaliable to rent. Please choose another one',
        'status': False,
    }

    def queryset(self, request):
        filters = self.filters(request=self.request)
        qs = Rent.objects.all()
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
        self.preparer.fields = self.fields
        create_rent = {
            'customer': Customer.objects.get(cpf=self.data['customer']),
            'vehicle': Vehicle.objects.get(slug=self.data['vehicle']),
            'mileage': self.data['mileage'],
            'date_checkout': self.data['date_checkout'],
            'date_checkin': self.data['date_checkin'],
        }
        try:
            get_vehicle = create_rent['vehicle']
            if not get_vehicle.is_avaliable:
                self.preparer.fields = self.error_fields
                return self.preparer.fields
            return Rent.objects.create(**create_rent)
        except:
            return False

    def update(self, pk):
        self.preparer.fields = self.fields
        try:
            up_rent = Rent.objects.get(id=pk)
        except Rent.DoesNotExist:
            return self.not_found(self.__class__.__name__, "ID", pk)
        up_rent.customer = Customer.objects.get(id=self.data['customer'])
        up_rent.vehicle = Vehicle.objects.get(id=self.data['vehicle'])
        up_rent.mileage = self.data['mileage']
        up_rent.date_checkout = self.data['date_checkout']
        up_rent.date_checkin = self.data['date_checkin']
        up_rent.save()
        return up_rent

    def delete(self, pk):
        return Rent.objects.get(id=pk).delete()

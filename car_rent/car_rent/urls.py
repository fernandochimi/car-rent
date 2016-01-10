# coding: utf-8
from django.conf.urls import url, patterns, include

from resources import TypeResource, BrandResource,\
    TransportResource, CityResource, MapResource


urlpatterns = patterns(
    '',
    url(r'^api/v1/type/', include(TypeResource.urls())),
    url(r'^api/v1/brand/', include(BrandResource.urls())),
    url(r'^api/v1/transport/', include(TransportResource.urls())),
    url(r'^api/v1/city/', include(CityResource.urls())),

    url(r'^api/v1/map/$', MapResource.as_list(), name='map_list'),
    url(
        r'^api/v1/map/(?P<slug>[-_\w]+)/$',
        MapResource.as_detail(), name='map_detail'),
    url(r'api/v1/get-map/$',
        MapResource.as_view('get_map'), name='get_map'),
)

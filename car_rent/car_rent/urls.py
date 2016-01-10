# coding: utf-8
from django.conf.urls import url, patterns, include

from resources import CustomerResource, VehicleResource,\
    RentResource


urlpatterns = patterns(
    '',
    url(r'^api/v1/customer/', include(CustomerResource.urls())),
    url(r'^api/v1/vehicle/', include(VehicleResource.urls())),
    url(r'^api/v1/rent/', include(RentResource.urls())),
)

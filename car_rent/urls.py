# coding: utf-8
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('walmart_log.urls')),
)

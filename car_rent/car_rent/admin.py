# coding: utf-8
from django.contrib import admin

from models import Token, Type, Brand, Transport, City, Map


class TokenAdmin(admin.ModelAdmin):
    list_display = ("token", "user", "date_added", "is_active",)
    list_filter = ("is_active",)
    date_hierarchy = "date_added"
    search_fields = ("user__username", "token",)


class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "date_added", "is_active",)
    list_filter = ("is_active",)
    date_hierarchy = "date_added"
    search_fields = ("name", "slug",)
    prepopulated_fields = {"slug": ("name",)}


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "date_added", "is_active",)
    list_filter = ("is_active",)
    date_hierarchy = "date_added"
    search_fields = ("name", "slug",)
    prepopulated_fields = {"slug": ("name",)}


class TransportAdmin(admin.ModelAdmin):
    list_display = ("name", "sign", "autonomy", "date_added", "is_active",)
    list_filter = ("transport_way", "transport_type", "brand", "is_active",)
    date_hierarchy = "date_added"
    search_fields = ("name", "slug", "sign",)
    prepopulated_fields = {"slug": ("name",)}


class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "date_added", "is_active",)
    list_filter = ("is_active",)
    date_hierarchy = "date_added"
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class MapAdmin(admin.ModelAdmin):
    list_display = (
        "name", "city_origin", "city_destiny",
        "date_added", "is_active", "cost_percent",)
    list_filter = ("is_active", "transport__name",)
    date_hierarchy = "date_added"
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("cost_percent", )


admin.site.register(Token, TokenAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Transport, TransportAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Map, MapAdmin)

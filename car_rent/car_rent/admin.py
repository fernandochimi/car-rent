# coding: utf-8
from django.contrib import admin

from models import Token, Customer, Vehicle, Rent


class TokenAdmin(admin.ModelAdmin):
    list_display = ("token", "user", "date_added", "is_active",)
    list_filter = ("is_active",)
    date_hierarchy = "date_added"
    search_fields = ("user__username", "token",)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "cpf", "cnh",)
    list_filter = ("cnh",)
    search_fields = ("name", "cpf")


class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "name", "vehicle_category", "date_added", "is_avaliable", "is_active",)
    list_filter = ("vehicle_category", "is_avaliable", "is_active",)
    date_hierarchy = "date_added"
    search_fields = ("name", "slug",)
    prepopulated_fields = {"slug": ("name",)}


class RentAdmin(admin.ModelAdmin):
    list_display = ("name", "sign", "autonomy", "date_added", "is_active",)
    list_filter = ("transport_way", "transport_type", "brand", "is_active",)
    date_hierarchy = "date_added"
    search_fields = ("name", "slug", "sign",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Token, TokenAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(Rent, RentAdmin)

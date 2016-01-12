# coding utf-8
import uuid

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from utils import unique_slugify, FORMAT_DATE

MOTORCYCLE, CAR, UTILITY, TRUCK = range(1, 5)

A, B, C, D, E = range(1, 6)

VEHICLES_CATEGORIES = (
    (MOTORCYCLE, u'Motorcycle'),
    (CAR, u'Car'),
    (UTILITY, u'Utility'),
    (TRUCK, u'Truck'),
)

CNH = (
    (A, u'A'),
    (B, u'B'),
    (C, u'C'),
    (D, u'D'),
    (E, u'E'),
)


class Token(models.Model):
    user = models.ForeignKey(
        User, related_name='token_set', null=True, blank=True)
    token = models.CharField(
        u'token', max_length=128, unique=True,
        default=uuid.uuid4, primary_key=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.token)

    class Meta:
        verbose_name, verbose_name_plural = "Token", "Token"


class Customer(models.Model):
    cnh = models.IntegerField(
        u'cnh', choices=CNH, default=CNH[1])
    name = models.CharField(u'name', max_length=255)
    cpf = models.CharField(u'cpf', max_length=11)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    class Meta:
        verbose_name, verbose_name_plural = "Customer", "Customers"


class Vehicle(models.Model):
    vehicle_category = models.IntegerField(
        u'vehicle_category',
        choices=VEHICLES_CATEGORIES,
        default=VEHICLES_CATEGORIES[1])
    name = models.CharField(
        u'name', max_length=255, help_text='Ex: Corsa Sedan')
    slug = models.SlugField(u'slug', unique=True)
    sign = models.CharField(
        u'sign', max_length=20, null=True, blank=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_avaliable = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def save(self, *args, **kwargs):
        slug_str = "%s" % self.name
        unique_slugify(self, slug_str)
        super(Vehicle, self).save(*args, **kwargs)

    class Meta:
        verbose_name, verbose_name_plural = "Vehicle", "Vehicles"


class Rent(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer_set')
    vehicle = models.ForeignKey(Vehicle, related_name='vehicle_set')
    mileage = models.DecimalField(
        u'mileage', default=0, decimal_places=2, max_digits=11,
        null=True, blank=True)
    date_checkout = models.DateTimeField(
        u'date checkout', null=True, blank=True)
    date_checkin = models.DateTimeField(
        u'date checkin', null=True, blank=True)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.customer.cpf, self.vehicle.name)

    def save(self, *args, **kwargs):
        if not self.vehicle.is_avaliable and (
                datetime.strptime(
                    self.date_checkin, FORMAT_DATE) >= datetime.today()):
            self.is_avaliable = True

        self.vehicle.is_avaliable = False
        self.vehicle.save()
        super(Rent, self).save(*args, **kwargs)

    class Meta:
        verbose_name, verbose_name_plural = "Rent", "Rents"

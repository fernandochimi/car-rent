# coding utf-8
import uuid

from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

from utils import unique_slugify

GROUND, AIR, WATER = range(1, 4)

TRANSPORT_WAY_CHOICES = (
    (GROUND, u'Ground'),
    (AIR, u'Air'),
    (WATER, u'Water'),
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


class Type(models.Model):
    name = models.CharField(
        u'name', help_text=u"Ex: Truck, Bus, Car", max_length=255)
    slug = models.SlugField(u'slug', unique=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def save(self, *args, **kwargs):
        slug_str = "%s" % self.name
        unique_slugify(self, slug_str)
        super(Type, self).save(*args, **kwargs)

    class Meta:
        verbose_name, verbose_name_plural = "Type", "Types"


class Brand(models.Model):
    name = models.CharField(
        u'name', help_text=u"Ex: Scania, Volvo", max_length=255)
    slug = models.SlugField(u'slug', unique=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def save(self, *args, **kwargs):
        slug_str = "%s" % self.name
        unique_slugify(self, slug_str)
        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name, verbose_name_plural = "Brand", "Brands"


class Transport(models.Model):
    transport_way = models.IntegerField(
        u'transport way',
        choices=TRANSPORT_WAY_CHOICES,
        default=TRANSPORT_WAY_CHOICES[0])
    transport_type = models.ForeignKey(Type)
    brand = models.ForeignKey(Brand)
    name = models.CharField(
        u'name', max_length=255, help_text='Ex: Marcopolo Audace 1050 HK')
    slug = models.SlugField(u'slug', unique=True)
    sign = models.CharField(
        u'sign', max_length=20, null=True, blank=True, unique=True)
    autonomy = models.DecimalField(
        u'autonomy', default=0, decimal_places=2, max_digits=8,
        help_text='On kilometers. Ex: 12.2')
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0} - {1}'.format(self.brand.name, self.name)

    def save(self, *args, **kwargs):
        slug_str = "%s" % self.name
        unique_slugify(self, slug_str)
        super(Transport, self).save(*args, **kwargs)

    class Meta:
        verbose_name, verbose_name_plural = "Transport", "Transports"


class City(models.Model):
    name = models.CharField(u'name', max_length=255, unique=True)
    slug = models.SlugField(u'slug', unique=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def save(self, *args, **kwargs):
        slug_str = "%s" % self.name
        unique_slugify(self, slug_str)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name, verbose_name_plural = "City", "Cities"


class Map(models.Model):
    name = models.CharField(
        u'name', help_text=u"Ex: SP Map, MG Map", max_length=255)
    slug = models.SlugField(u'slug', unique=True)
    transport = models.ForeignKey(Transport, related_name='transport_set')
    city_origin = models.ForeignKey(City, related_name='cityorigin_set')
    city_destiny = models.ForeignKey(City, related_name='citydestiny_set')
    logistic_order = models.TextField(null=True, blank=True)
    total_distance = models.DecimalField(
        u'total distance', default=0, decimal_places=2, max_digits=11,
        null=True, blank=True)
    gas_value = models.DecimalField(
        u'gas value', default=0, decimal_places=2, max_digits=11,
        help_text='On KM', null=True, blank=True)
    cost_percent = models.DecimalField(
        u'cost percent', default=0, decimal_places=2, max_digits=11,
        null=True, blank=True)
    date_added = models.DateTimeField(
        default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def save(self, *args, **kwargs):
        slug_str = "%s" % self.name
        unique_slugify(self, slug_str)
        self.cost_percent = (
            self.total_distance * self.gas_value) / self.transport.autonomy
        super(Map, self).save(*args, **kwargs)

    class Meta:
        verbose_name, verbose_name_plural = "Map", "Maps"

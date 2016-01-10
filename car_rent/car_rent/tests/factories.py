# coding: utf-8
import factory
import factory.fuzzy
import uuid

from datetime import datetime

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from walmart_log.models import Token, Type,\
     Brand, Transport, City, Map, TRANSPORT_WAY_CHOICES


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: u"user%s" % n)
    first_name = factory.Sequence(lambda n: u"User %s" % n)
    last_name = factory.Sequence(lambda n: u"Final Name %s" % n)


class TokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Token

    user = factory.SubFactory(UserFactory)
    token = uuid.uuid4()
    date_added = datetime.now()
    is_active = True


class TypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Type

    name = factory.Sequence(lambda n: u"Type %s" % n)
    slug = factory.LazyAttributeSequence(
        lambda o, n: u"%s-%d" % (slugify(o.name), n))
    date_added = datetime.now()
    is_active = True


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.Sequence(lambda n: u"Brand %s" % n)
    slug = factory.LazyAttributeSequence(
        lambda o, n: u"%s-%d" % (slugify(o.name), n))
    date_added = datetime.now()
    is_active = True


class TransportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transport

    transport_way = factory.Iterator(
        TRANSPORT_WAY_CHOICES, getter=lambda c: c[0])
    transport_type = factory.SubFactory(TypeFactory)
    brand = factory.SubFactory(BrandFactory)
    name = factory.Sequence(lambda n: u"Vehicle %s" % n)
    slug = factory.LazyAttributeSequence(
        lambda o, n: u"%s-%d" % (slugify(o.name), n))
    sign = factory.Sequence(lambda n: u"XXX-00%s" % n)
    autonomy = factory.fuzzy.FuzzyDecimal(0.1, 99.9, 2)
    date_added = datetime.now()
    is_active = True


class CityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = City

    name = factory.Sequence(lambda n: u"City%s" % n)
    slug = factory.LazyAttributeSequence(
        lambda o, n: u"%s-%d" % (slugify(o.name), n))
    date_added = datetime.now()
    is_active = True


class MapFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Map

    name = factory.Sequence(lambda n: u"Map%s" % n)
    slug = factory.LazyAttributeSequence(
        lambda o, n: u"%s-%d" % (slugify(o.name), n))
    transport = factory.SubFactory(TransportFactory)
    city_origin = factory.SubFactory(CityFactory)
    city_destiny = factory.SubFactory(CityFactory)
    logistic_order = factory.Sequence(lambda n: "City %s" % n)
    total_distance = factory.fuzzy.FuzzyDecimal(0.1, 99.9, 2)
    gas_value = factory.fuzzy.FuzzyDecimal(0.1, 99.9, 2)
    cost_percent = factory.fuzzy.FuzzyDecimal(0.1, 99.9, 2)
    date_added = datetime.now()
    is_active = True

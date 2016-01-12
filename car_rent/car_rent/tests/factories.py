# coding: utf-8
import factory
import factory.fuzzy
import uuid

from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from car_rent.models import Token, Customer,\
     Vehicle, Rent, VEHICLES_CATEGORIES, CNH


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


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    cnh = factory.Iterator(
        CNH, getter=lambda c: c[0])
    name = factory.Sequence(lambda n: u"Customer %s" % n)
    cpf = factory.Sequence(lambda n: u"000.000.000-0%s" % n)


class VehicleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vehicle

    vehicle_category = factory.Iterator(
        VEHICLES_CATEGORIES, getter=lambda c: c[0])
    name = factory.Sequence(lambda n: u"Vehicle %s" % n)
    slug = factory.LazyAttributeSequence(
        lambda o, n: u"%s-%d" % (slugify(o.name), n))
    sign = factory.Sequence(lambda n: u"XXX-00%s" % n)
    date_added = datetime.now()
    is_avaliable = True
    is_active = True


class RentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rent

    customer = factory.SubFactory(CustomerFactory)
    vehicle = factory.SubFactory(VehicleFactory)
    mileage = factory.fuzzy.FuzzyDecimal(0.1, 99.9, 2)
    date_checkout = datetime.now()
    date_checkin = datetime.now() + relativedelta(days=1)

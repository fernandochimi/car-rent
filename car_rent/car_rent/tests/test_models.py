# coding: utf-8
from django.test import TestCase

from factories import TokenFactory,\
    CustomerFactory, VehicleFactory, RentFactory


class TokenTest(TestCase):
    def setUp(self):
        self.token = TokenFactory()

    def test_01_unicode(self):
        "Token must be a unicode"
        self.assertEqual(unicode(self.token), u"{0}".format(self.token.token))


class CustomerTest(TestCase):
    def setUp(self):
        self.customer = CustomerFactory()

    def test_01_unicode(self):
        "Customer must be a unicode"
        self.assertEqual(
            unicode(self.customer), u"{0}".format(self.customer.name))


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = VehicleFactory()

    def test_01_unicode(self):
        "Vehicle must be a unicode"
        self.assertEqual(
            unicode(self.vehicle), u"{0}".format(self.vehicle.name))


class RentTest(TestCase):
    def setUp(self):
        self.rent = RentFactory()

    def test_01_unicode(self):
        "Rent must be a unicode"
        self.assertEqual(unicode(self.rent), u"{0} - {1}".format(
            self.rent.customer.cpf, self.rent.vehicle.name))

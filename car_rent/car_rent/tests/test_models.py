# coding: utf-8
from django.test import TestCase

from factories import TokenFactory, TypeFactory, BrandFactory,\
    TransportFactory, CityFactory, MapFactory


class TokenTest(TestCase):
    def setUp(self):
        self.token = TokenFactory()

    def test_01_unicode(self):
        "Token must be a unicode"
        self.assertEqual(unicode(self.token), u"{0}".format(self.token.token))


class TypeTest(TestCase):
    def setUp(self):
        self.type = TypeFactory()

    def test_01_unicode(self):
        "Type must be a unicode"
        self.assertEqual(unicode(self.type), u"{0}".format(self.type.name))


class BrandTest(TestCase):
    def setUp(self):
        self.brand = BrandFactory()

    def test_01_unicode(self):
        "Brand must be a unicode"
        self.assertEqual(unicode(self.brand), u"{0}".format(self.brand.name))


class TransportTest(TestCase):
    def setUp(self):
        self.transport = TransportFactory()

    def test_01_unicode(self):
        "Transport must be a unicode"
        self.assertEqual(unicode(self.transport), u"{0} - {1}".format(
            self.transport.brand.name, self.transport.name))


class CityTest(TestCase):
    def setUp(self):
        self.city = CityFactory()

    def test_01_unicode(self):
        "City must be a unicode"
        self.assertEqual(unicode(self.city), u"{0}".format(self.city.name))


class MapTest(TestCase):
    def setUp(self):
        self.map = MapFactory()

    def test_01_unicode(self):
        "Map must be a unicode"
        self.assertEqual(unicode(self.map), u"{0}".format(self.map.name))

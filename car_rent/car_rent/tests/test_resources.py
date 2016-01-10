# coding: utf-8
import json
import factory

from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.test import TestCase

from car_rent.tasks import create_map
from car_rent.utils import jdefault

from factories import TokenFactory, CustomerFactory,\
    VehicleFactory, RentFactory


class BaseResourceTest(TestCase):
    def setUp(self):
        self.token = TokenFactory()
        self.customer = CustomerFactory()
        self.vehicle = VehicleFactory()
        self.rent = RentFactory()

        self.new_customer = CustomerFactory.create(
            cnh=1,
            name=u"Fulano de Tal",
            cpf="780.089.098-88",
        )
        self.new_vehicle = VehicleFactory.create(
            vehicle_category=1,
            name=u"New Vehicle",
            slug="new-vehicle",
            sign="XXX",
            date_added=datetime.now(),
            is_avaliable=True,
            is_active=True,
        )
        self.new_rent = RentFactory.create(
            customer=factory.SubFactory(CustomerFactory),
            vehicle=factory.SubFactory(VehicleFactory),
            mileage="10.0",
            date_checkout=datetime.now(),
            date_checkin=datetime.now() + relativedelta(days=2),
        )

    def test_01_unauthorized(self):
        "Request without token does not pass"
        response = self.client.get("/api/v1/type/")
        self.assertEqual(response.status_code, 401)

# class TypeResourceTest(BaseResourceTest):
#     def test_01_list_types(self):
#         "List all types"
#         response = self.client.get("/api/v1/type/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_02_detail_type(self):
#         "Detail a type"
#         response = self.client.get("/api/v1/type/{0}/?token={1}".format(
#             self.type.id, self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_03_type_does_not_exist(self):
#         "Type does not exist"
#         response = self.client.get("/api/v1/type/0/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 404)

#     def test_04_create_type(self):
#         "Create a type"
#         response = self.client.post("/api/v1/type/?token={0}".format(
#             self.token.token), json.dumps(self.new_type, default=jdefault),
#             content_type="application/json")
#         self.assertEqual(response.status_code, 201)

#     def test_05_update_type(self):
#         "Update a type"
#         self.new_type.slug = "new-update-type"
#         self.new_type.save()
#         response = self.client.put("/api/v1/type/{0}/?token={1}".format(
#             self.new_type.id, self.token.token),
#             json.dumps(self.new_type, default=jdefault))
#         self.assertEqual(response.status_code, 202)

#     def test_06_update_type_does_not_exist(self):
#         "Update a type that does not exist"
#         self.new_type.slug = "new-update-type"
#         self.new_type.save()
#         response = self.client.put("/api/v1/type/0/?token={1}".format(
#             self.new_type.id, self.token.token),
#             json.dumps(self.new_type, default=jdefault))
#         self.assertEqual(response.status_code, 404)

#     def test_05_delete_type(self):
#         "Delete a type"
#         response = self.client.delete("/api/v1/type/{0}/?token={1}".format(
#             self.new_type.id, self.token.token))
#         self.assertEqual(response.status_code, 204)


# class BrandResourceTest(BaseResourceTest):
#     def test_01_list_brands(self):
#         "List all brands"
#         response = self.client.get("/api/v1/brand/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_02_detail_brand(self):
#         "Detail a brand"
#         response = self.client.get("/api/v1/brand/{0}/?token={1}".format(
#             self.brand.id, self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_03_brand_does_not_exist(self):
#         "Brand does not exist"
#         response = self.client.get("/api/v1/brand/0/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 404)

#     def test_04_create_brand(self):
#         "Create a brand"

#         response = self.client.post("/api/v1/brand/?token={0}".format(
#             self.token.token), json.dumps(self.new_brand, default=jdefault),
#             content_type="application/json")
#         self.assertEqual(response.status_code, 201)

#     def test_05_update_brand(self):
#         "Update a brand"
#         self.new_brand.slug = "new-update-brand"
#         self.new_brand.save()
#         response = self.client.put("/api/v1/brand/{0}/?token={1}".format(
#             self.new_brand.id, self.token.token),
#             json.dumps(self.new_brand, default=jdefault))
#         self.assertEqual(response.status_code, 202)

#     def test_06_update_brand_does_not_exist(self):
#         "Update a brand that does not exist"
#         self.new_brand.slug = "new-update-brand"
#         self.new_brand.save()
#         response = self.client.put("/api/v1/brand/0/?token={1}".format(
#             self.new_brand.id, self.token.token),
#             json.dumps(self.new_brand, default=jdefault))
#         self.assertEqual(response.status_code, 404)

#     def test_05_delete_brand(self):
#         "Delete a brand"
#         response = self.client.delete("/api/v1/brand/{0}/?token={1}".format(
#             self.new_brand.id, self.token.token))
#         self.assertEqual(response.status_code, 204)


# class TransportResourceTest(BaseResourceTest):
#     def test_01_list_transports(self):
#         "List all transports"
#         response = self.client.get("/api/v1/transport/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_02_detail_transport(self):
#         "Detail a transport"
#         response = self.client.get("/api/v1/transport/{0}/?token={1}".format(
#             self.transport.id, self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_03_transport_does_not_exist(self):
#         "Transport does not exist"
#         response = self.client.get("/api/v1/transport/0/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 404)

#     def test_04_create_transport(self):
#         "Create a transport"
#         print json.dumps(self.new_transport, default=jdefault)
#         response = self.client.post("/api/v1/transport/?token={0}".format(
#             self.token.token), json.dumps(
#             self.new_transport, default=jdefault),
#             content_type="application/json")
#         print response
#         self.assertEqual(response.status_code, 201)

#     def test_05_update_transport(self):
#         "Update a transport"
#         self.new_transport.slug = "new-update-transport"
#         self.new_transport.save()
#         response = self.client.put("/api/v1/transport/{0}/?token={1}".format(
#             self.new_transport.id, self.token.token),
#             json.dumps(self.new_transport, default=jdefault))
#         self.assertEqual(response.status_code, 202)

#     def test_06_update_transport_does_not_exist(self):
#         "Update a transport that does not exist"
#         self.new_transport.slug = "new-update-transport"
#         self.new_transport.save()
#         response = self.client.put("/api/v1/transport/0/?token={1}".format(
#             self.new_transport.id, self.token.token),
#             json.dumps(self.new_transport, default=jdefault))
#         self.assertEqual(response.status_code, 404)


# class CityResourceTest(BaseResourceTest):
#     def test_01_list_cities(self):
#         "List all cities"
#         response = self.client.get("/api/v1/city/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_02_detail_city(self):
#         "Detail a city"
#         response = self.client.get("/api/v1/city/{0}/?token={1}".format(
#             self.city.id, self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_03_city_does_not_exist(self):
#         "City does not exist"
#         response = self.client.get("/api/v1/city/0/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 404)


# class MapResourceTest(BaseResourceTest):
#     def test_01_list_maps(self):
#         "List all maps"
#         response = self.client.get("/api/v1/map/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_02_detail_map(self):
#         "Detail a map"
#         response = self.client.get("/api/v1/map/{0}/?token={1}".format(
#             self.map.slug, self.token.token))
#         self.assertEqual(response.status_code, 200)

#     def test_03_map_does_not_exist(self):
#         "Map does not exist"
#         response = self.client.get("/api/v1/map/0/?token={0}".format(
#             self.token.token))
#         self.assertEqual(response.status_code, 404)

#     def test_04_create_map(self):
#         "Create a map"
#         response = self.client.post("/api/v1/get-map/?token={0}".format(
#             self.token.token), json.dumps(self.new_map, default=jdefault))
#         create_new_map = create_map.delay(self.new_map)
#         self.assertTrue(create_new_map, "new-map")
#         self.assertEqual(response.status_code, 201)

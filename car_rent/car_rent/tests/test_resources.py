# coding: utf-8
import json
import factory

from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.test import TestCase

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
            slug=u"new-vehicle",
            sign=u"XXX-123",
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
        response = self.client.get("/api/v1/customer/")
        self.assertEqual(response.status_code, 401)


class CustomerResourceTest(BaseResourceTest):
    def test_01_list_customers(self):
        "List all customers"
        response = self.client.get("/api/v1/customer/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_02_detail_customer(self):
        "Detail a customer"
        response = self.client.get("/api/v1/customer/{0}/?token={1}".format(
            self.customer.id, self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_03_customer_does_not_exist(self):
        "Customer does not exist"
        response = self.client.get("/api/v1/customer/0/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 404)

    def test_04_create_customer(self):
        "Create a customer"
        response = self.client.post("/api/v1/customer/?token={0}".format(
            self.token.token), json.dumps(self.new_customer, default=jdefault),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_05_update_customer(self):
        "Update a customer"
        self.new_customer.slug = "new-update-customer"
        self.new_customer.save()
        response = self.client.put("/api/v1/customer/{0}/?token={1}".format(
            self.new_customer.id, self.token.token),
            json.dumps(self.new_customer, default=jdefault))
        self.assertEqual(response.status_code, 202)

    def test_06_update_customer_does_not_exist(self):
        "Update a customer that does not exist"
        self.new_customer.slug = "new-update-customer"
        self.new_customer.save()
        response = self.client.put("/api/v1/customer/0/?token={1}".format(
            self.new_customer.id, self.token.token),
            json.dumps(self.new_customer, default=jdefault))
        self.assertEqual(response.status_code, 404)

    def test_05_delete_customer(self):
        "Delete a customer"
        response = self.client.delete("/api/v1/customer/{0}/?token={1}".format(
            self.new_customer.id, self.token.token))
        self.assertEqual(response.status_code, 204)


class VehicleResourceTest(BaseResourceTest):
    def test_01_list_vehicles(self):
        "List all vehicles"
        response = self.client.get("/api/v1/vehicle/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_02_detail_vehicle(self):
        "Detail a vehicle"
        response = self.client.get("/api/v1/vehicle/{0}/?token={1}".format(
            self.vehicle.id, self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_03_vehicle_does_not_exist(self):
        "Vehicle does not exist"
        response = self.client.get("/api/v1/vehicle/0/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 404)

    def test_04_create_vehicle(self):
        "Create a vehicle"
        response = self.client.post("/api/v1/vehicle/?token={0}".format(
            self.token.token), json.dumps(self.new_vehicle, default=jdefault),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_05_update_vehicle(self):
        "Update a vehicle"
        self.new_vehicle.slug = "new-update-vehicle"
        self.new_vehicle.save()
        response = self.client.put("/api/v1/vehicle/{0}/?token={1}".format(
            self.new_vehicle.id, self.token.token),
            json.dumps(self.new_vehicle, default=jdefault))
        self.assertEqual(response.status_code, 202)

    def test_06_update_vehicle_does_not_exist(self):
        "Update a vehicle that does not exist"
        self.new_vehicle.slug = "new-update-vehicle"
        self.new_vehicle.save()
        response = self.client.put("/api/v1/vehicle/0/?token={1}".format(
            self.new_vehicle.id, self.token.token),
            json.dumps(self.new_vehicle, default=jdefault))
        self.assertEqual(response.status_code, 404)

    def test_05_delete_vehicle(self):
        "Delete a vehicle"
        response = self.client.delete("/api/v1/vehicle/{0}/?token={1}".format(
            self.new_vehicle.id, self.token.token))
        self.assertEqual(response.status_code, 204)


class RentResourceTest(BaseResourceTest):
    def test_01_list_rents(self):
        "List all rents"
        response = self.client.get("/api/v1/rent/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_02_detail_rent(self):
        "Detail a rent"
        response = self.client.get("/api/v1/rent/{0}/?token={1}".format(
            self.rent.id, self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_03_rent_does_not_exist(self):
        "Rent does not exist"
        response = self.client.get("/api/v1/rent/0/?token={0}".format(
            self.token.token))
        self.assertEqual(response.status_code, 404)

    # def test_04_create_rent(self):
    #     "Create a rent"
    #     print json.dumps(self.new_rent, default=jdefault)
    #     response = self.client.post("/api/v1/rent/?token={0}".format(
    #         self.token.token), json.dumps(
    #         self.new_rent, default=jdefault),
    #         content_type="application/json")
    #     print response
    #     self.assertEqual(response.status_code, 201)

    # def test_05_update_rent(self):
    #     "Update a rent"
    #     self.new_rent.slug = "new-update-rent"
    #     self.new_rent.save()
    #     response = self.client.put("/api/v1/rent/{0}/?token={1}".format(
    #         self.new_rent.id, self.token.token),
    #         json.dumps(self.new_rent, default=jdefault))
    #     self.assertEqual(response.status_code, 202)

    # def test_06_update_rent_does_not_exist(self):
    #     "Update a rent that does not exist"
    #     self.new_rent.slug = "new-update-rent"
    #     self.new_rent.save()
    #     response = self.client.put("/api/v1/rent/0/?token={1}".format(
    #         self.new_rent.id, self.token.token),
    #         json.dumps(self.new_rent, default=jdefault))
    #     self.assertEqual(response.status_code, 404)

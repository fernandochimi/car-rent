Walmart Log
================

Intro
----------------
The Walmart Log Project was developed to manage and help the logistic team of the Company.
This is a solution that envolved a better cost benefit to delivery products from city to another city with every transport.

The project was developed in Python 2.7, with Django Framework 1.8, combined with Redis server 3. It is work to give a best performance to the system.


Requirements
----------------
To use Walmart Log, you need to install some libraries and modules:

	* sudo apt-get install libffi-dev libssl-dev
	* redis
	* virtualenvwrapper
	* Python 2.7
::


After you complete the instalation of libraries, you can install this:
::
	$ pip install -r requirements.txt


Types
----------------
To create a new Type, put the code below on terminal:
::
	$ curl -X POST -H "Content-Type: application/json" -d '{"name": "Caminhão", "slug": "caminhao"}' http://localhost:8000/api/v1/type/?token={valid-token}

Response:
::
	{
		"date_added": "2015-10-04 00:00:00",
		"is_active": true,
		"name": "Caminhão",
		"slug": "caminhao",
	}

curl -X GET http://localhost:8000/api/v1/type/?token={valid}

Brand
----------------
To create a new Brand, put the code below on terminal:
::
	$ curl -X POST -H "Content-Type: application/json" -d '{"name": "Scania", "slug": "scania"}' http://localhost:8000/api/v1/brand/?token={valid-token}

Response:
::
	{
		"is_active": true,
		"date_added": "2015-10-04 00:00:00",
		"name": "Scania",
		"slug": "scania",
	}

Transport
----------------
To create a new Transport, put the code below on terminal:
::
	$ curl -X POST -H "Content-Type: application/json" -d '{"transport_way": 1, "transport_type": "caminhao", "brand": "scania", "name": "Scania L10", "slug": "scania-l10", "sign": "XXX-9999", "autonomy": "14.2"}' http://localhost:8000/api/v1/transport/?token={valid-token}

Response:
::

	{
		"name": "Caminhão",
		"slug": "caminhao",
	}

Maps
----------------
To create a new Type, put the code below on terminal:
::
	$curl -X POST -H "Content-Type: application/json" -d '{"name": "Caminhão", "slug": "caminhao"}' http://localhost:8000/api/v1/type/?token={valid-token}

Response:
::
	{
		"name": "Caminhão",
		"slug": "caminhao",
	}

This is a demo project.

Tests
----------------

Docs
----------------
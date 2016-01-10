# coding: utf-8
import logging

from decimal import Decimal

from settings import celery_app

from models import City, Map, Transport

logger = logging.getLogger('walmart_log.walmart_log.tasks')


@celery_app.task
def create_map(map_info):
    logger.info(u"Start creation of city {0}".format(map_info['city_origin']))
    city_origin, created = City.objects.get_or_create(
        name=map_info['city_origin'],
    )
    logger.info(
        u"City {0} created with success".format(map_info['city_origin']))

    logger.info(
        u"Start creation of city {0}".format(map_info['city_destiny']))
    city_destiny, created = City.objects.get_or_create(
        name=map_info['city_destiny'],
    )
    logger.info(
        u"City {0} created with success".format(map_info['city_destiny']))

    logger.info(
        u"Start creation of Map {0}".format(map_info['name']))
    route_map, created = Map.objects.get_or_create(
        name=map_info['name'],
        transport=Transport.objects.get(sign=map_info['transport_sign']),
        city_origin=City.objects.get(slug=city_origin.slug),
        city_destiny=City.objects.get(slug=city_destiny.slug),
        logistic_order=", ".join([i for i in map_info['logistic_order']]),
        total_distance=map_info['total_distance'],
        gas_value=Decimal(map_info['gas_value'].replace(",", ".")))
    logger.info(
        u"Map {0} created with success".format(map_info['name']))

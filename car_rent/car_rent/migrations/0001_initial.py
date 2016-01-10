# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.conf import settings
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cnh', models.IntegerField(default=(2, 'B'), verbose_name='cnh', choices=[(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')])),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('cpf', models.CharField(max_length=14, verbose_name='cpf')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mileage', models.DecimalField(decimal_places=2, default=0, max_digits=11, blank=True, null=True, verbose_name='mileage')),
                ('date_checkout', models.DateTimeField(null=True, verbose_name='date checkout', blank=True)),
                ('date_checkin', models.DateTimeField(null=True, verbose_name='date checkin', blank=True)),
                ('customer', models.ForeignKey(related_name='customer_set', to='car_rent.Customer')),
            ],
            options={
                'verbose_name': 'Rent',
                'verbose_name_plural': 'Rents',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token', models.CharField(primary_key=True, default=uuid.uuid4, serialize=False, max_length=128, unique=True, verbose_name='token')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(related_name='token_set', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Token',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vehicle_category', models.IntegerField(default=(2, 'Car'), verbose_name='vehicle_category', choices=[(1, 'Motorcycle'), (2, 'Car'), (3, 'Utility'), (4, 'Truck')])),
                ('name', models.CharField(help_text=b'Ex: Corsa Sedan', max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('sign', models.CharField(max_length=20, unique=True, null=True, verbose_name='sign', blank=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('is_avaliable', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
            },
        ),
        migrations.AddField(
            model_name='rent',
            name='vehicle',
            field=models.ForeignKey(related_name='vehicle_set', to='car_rent.Vehicle'),
        ),
    ]

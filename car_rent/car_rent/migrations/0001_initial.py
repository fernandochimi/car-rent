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
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Ex: Scania, Volvo', max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brands',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Ex: SP Map, MG Map', max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('gas_value', models.DecimalField(decimal_places=2, default=0, max_digits=5, blank=True, null=True, verbose_name='gas value')),
                ('other_coasts', models.DecimalField(decimal_places=2, default=0, max_digits=5, blank=True, null=True, verbose_name='other coasts')),
                ('coast_percent', models.DecimalField(decimal_places=2, default=0, max_digits=5, blank=True, null=True, verbose_name='coast percent')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('city_destiny', models.ForeignKey(related_name='citydestiny_set', to='walmart_log.City')),
                ('city_origin', models.ForeignKey(related_name='cityorigin_set', to='walmart_log.City')),
            ],
            options={
                'verbose_name': 'Map',
                'verbose_name_plural': 'Maps',
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
            name='Transport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transport_way', models.IntegerField(default=(1, 'Ground'), verbose_name='transport way', choices=[(1, 'Ground'), (2, 'Air'), (3, 'Water')])),
                ('name', models.CharField(help_text=b'Ex: Marcopolo Audace 1050 HK', max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('sign', models.CharField(max_length=20, null=True, verbose_name='sign', blank=True)),
                ('autonomy', models.DecimalField(default=0, help_text=b'On kilometers. Ex: 12.2', verbose_name='autonomy', max_digits=8, decimal_places=2)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(to='walmart_log.Brand')),
            ],
            options={
                'verbose_name': 'Transport',
                'verbose_name_plural': 'Transports',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text='Ex: Truck, Bus, Car', max_length=255, verbose_name='name')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('date_added', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Type',
                'verbose_name_plural': 'Types',
            },
        ),
        migrations.AddField(
            model_name='transport',
            name='transport_type',
            field=models.ForeignKey(to='walmart_log.Type'),
        ),
        migrations.AddField(
            model_name='map',
            name='transport',
            field=models.ForeignKey(related_name='transport_set', to='walmart_log.Transport'),
        ),
    ]

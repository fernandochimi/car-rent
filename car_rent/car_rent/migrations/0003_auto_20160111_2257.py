# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent', '0002_auto_20160110_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cpf',
            field=models.CharField(unique=True, max_length=11, verbose_name='cpf'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent', '0005_auto_20160112_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='sign',
            field=models.CharField(max_length=20, null=True, verbose_name='sign', blank=True),
        ),
    ]

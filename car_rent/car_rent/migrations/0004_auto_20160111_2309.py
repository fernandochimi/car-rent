# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_rent', '0003_auto_20160111_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='sign',
            field=models.CharField(max_length=20, unique=True, null=True, verbose_name='sign', blank=True),
        ),
    ]

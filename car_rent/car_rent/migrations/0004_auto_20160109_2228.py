# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walmart_log', '0003_auto_20160109_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='cost_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, blank=True, null=True, verbose_name='coast percent'),
        ),
        migrations.AlterField(
            model_name='map',
            name='gas_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, blank=True, null=True, verbose_name='gas value'),
        ),
        migrations.AlterField(
            model_name='map',
            name='total_distance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, blank=True, null=True, verbose_name='total distance'),
        ),
    ]

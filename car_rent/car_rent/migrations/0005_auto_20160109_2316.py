# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walmart_log', '0004_auto_20160109_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='cost_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, blank=True, null=True, verbose_name='cost percent'),
        ),
        migrations.AlterField(
            model_name='map',
            name='gas_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11, blank=True, help_text=b'On KM', null=True, verbose_name='gas value'),
        ),
    ]

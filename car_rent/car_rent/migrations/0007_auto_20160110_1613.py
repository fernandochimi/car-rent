# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walmart_log', '0006_map_logistic_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='slug',
            field=models.SlugField(verbose_name='slug'),
        ),
    ]

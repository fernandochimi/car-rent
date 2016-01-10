# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walmart_log', '0007_auto_20160110_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug'),
        ),
    ]

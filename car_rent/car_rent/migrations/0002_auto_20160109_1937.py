# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walmart_log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transport',
            name='sign',
            field=models.CharField(max_length=20, unique=True, null=True, verbose_name='sign', blank=True),
        ),
    ]

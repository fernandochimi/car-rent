# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walmart_log', '0005_auto_20160109_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='logistic_order',
            field=models.TextField(null=True, blank=True),
        ),
    ]

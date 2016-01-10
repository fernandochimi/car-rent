# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walmart_log', '0002_auto_20160109_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='map',
            old_name='coast_percent',
            new_name='cost_percent',
        ),
        migrations.RemoveField(
            model_name='map',
            name='other_coasts',
        ),
        migrations.AddField(
            model_name='map',
            name='total_distance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, blank=True, null=True, verbose_name='total distance'),
        ),
    ]

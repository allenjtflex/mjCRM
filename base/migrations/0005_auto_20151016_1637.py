# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20151016_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effective',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151016_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='effective',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 16, 8, 29, 43, 619482, tzinfo=utc)),
        ),
    ]

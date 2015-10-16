# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151016_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 10, 16, 8, 26, 4, 85095, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='update_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 10, 16, 8, 26, 22, 832872, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='effective',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 16, 8, 25, 2, 37404, tzinfo=utc)),
        ),
    ]

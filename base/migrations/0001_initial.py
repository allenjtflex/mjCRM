# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('cust_num', models.CharField(unique=True, max_length=8)),
                ('title', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('sales', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Effective',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('effective_month', models.IntegerField(default=14)),
                ('effective_mode', models.IntegerField(default=9)),
                ('start_date', models.DateField(default=datetime.datetime(2015, 10, 16, 4, 26, 16, 354796, tzinfo=utc))),
                ('end_date', models.DateField(default=datetime.date(2050, 12, 31))),
                ('is_valid', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(to='base.Customer')),
            ],
        ),
    ]

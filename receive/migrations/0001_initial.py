# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rejection',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('deliver', models.CharField(max_length=30)),
                ('deliver_num', models.CharField(max_length=30)),
                ('cctno', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('wmemo', models.TextField(blank=True, null=True)),
                ('smemo', models.TextField(blank=True, null=True)),
                ('deliver_at', models.DateField(default=datetime.datetime(2015, 10, 16, 4, 26, 16, 358059, tzinfo=utc))),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(to='base.Customer')),
            ],
        ),
    ]

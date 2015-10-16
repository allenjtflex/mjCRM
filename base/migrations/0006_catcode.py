# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20151016_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catcode',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('scode', models.CharField(max_length=4)),
                ('tcode', models.CharField(blank=True, max_length=4, null=True)),
                ('item', models.CharField(blank=True, max_length=4, null=True)),
                ('describtion', models.CharField(max_length=60)),
                ('describtion2', models.CharField(blank=True, max_length=60, null=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('bformat', models.CharField(max_length=4)),
                ('barcodelen', models.IntegerField()),
                ('regexpstring', models.CharField(max_length=254)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

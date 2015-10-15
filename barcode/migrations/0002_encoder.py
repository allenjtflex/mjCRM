# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encoder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('caption', models.CharField(max_length=4)),
                ('start_position', models.IntegerField()),
                ('char_length', models.IntegerField()),
                ('bformat', models.ForeignKey(to='barcode.Barcode')),
            ],
        ),
    ]

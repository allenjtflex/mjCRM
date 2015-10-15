# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0002_encoder'),
    ]

    operations = [
        migrations.CreateModel(
            name='Definecaption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='encoder',
            name='caption',
            field=models.ForeignKey(to='barcode.Definecaption'),
        ),
    ]

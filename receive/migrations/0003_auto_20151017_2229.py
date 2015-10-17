# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receive', '0002_auto_20151016_2254'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rejection',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='rejection',
            name='cctno',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rejection',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]

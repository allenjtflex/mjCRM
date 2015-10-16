# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20151016_1731'),
        ('receive', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rejection',
            name='uom',
            field=models.ForeignKey(default=1, to='base.Catcode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rejection',
            name='deliver_at',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]

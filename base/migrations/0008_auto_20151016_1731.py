# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20151016_1731'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='catcode',
            unique_together=set([('scode', 'tcode', 'icode')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barcode', '0003_auto_20151015_1651'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barcode',
            options={'ordering': ['bformat']},
        ),
        migrations.AlterModelOptions(
            name='definecaption',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='encoder',
            options={'ordering': ['bformat', 'start_position']},
        ),
    ]

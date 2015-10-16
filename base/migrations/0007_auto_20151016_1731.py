# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_catcode'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catcode',
            old_name='item',
            new_name='icode',
        ),
        migrations.AddField(
            model_name='catcode',
            name='is_embedded',
            field=models.BooleanField(default=True),
        ),
    ]

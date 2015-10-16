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
            name='Person',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='effective',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2015, 10, 16, 8, 18, 26, 721139, tzinfo=utc)),
        ),
    ]

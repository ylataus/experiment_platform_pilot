# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 17:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0015_auto_20160721_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='crowd',
            name='creation_date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-27 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0004_auto_20160927_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='calaccess_processed.Election'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-22 06:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calaccess_processed', '0029_auto_20161122_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propositioncommittee',
            name='position',
        ),
        migrations.RemoveField(
            model_name='propositioncommittee',
            name='proposition',
        ),
    ]
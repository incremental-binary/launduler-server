# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170605_1806'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alternative',
            old_name='location',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='alternative',
            old_name='phoneNum',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='alternative',
            old_name='serviceName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='alternative',
            name='price',
        ),
    ]

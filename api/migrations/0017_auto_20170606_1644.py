# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20170606_1625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machineuser',
            name='location',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='scheduledAt',
            field=models.DateTimeField(default=b'2017-06-06 16:44:42'),
        ),
        migrations.DeleteModel(
            name='MachineUser',
        ),
    ]

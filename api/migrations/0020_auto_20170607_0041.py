# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20170606_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='scheduledAt',
            field=models.DateTimeField(default=b'2017-06-07 00:41:48'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 08:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20170606_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='api.Machine'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='scheduledAt',
            field=models.DateTimeField(default=b'2017-06-06 17:38:54'),
        ),
    ]
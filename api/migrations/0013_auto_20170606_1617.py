# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 07:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20170606_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failure',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Machine'),
        ),
        migrations.AlterField(
            model_name='machine',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Place'),
        ),
        migrations.AlterField(
            model_name='machineuser',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Place'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Machine'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='scheduledAt',
            field=models.DateTimeField(default=b'2017-06-06 16:17:12'),
        ),
    ]

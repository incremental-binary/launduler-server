# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 09:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170605_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failure',
            name='reporterId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MachineUser', to_field='userId'),
        ),
        migrations.AlterField(
            model_name='machineuser',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Place', to_field='location'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MachineUser', to_field='userId'),
        ),
    ]
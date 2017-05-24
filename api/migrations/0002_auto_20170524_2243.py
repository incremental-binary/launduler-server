# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceName', models.CharField(default='none', max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('phoneNum', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Failure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine', models.CharField(default='none', max_length=255)),
                ('type', models.CharField(default='none', max_length=255)),
                ('comment', models.TextField()),
                ('reporterId', models.CharField(max_length=255)),
                ('isFixed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Userguide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guideName', models.CharField(default='none', max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='machine',
            old_name='name',
            new_name='serialNum',
        ),
        migrations.AddField(
            model_name='machine',
            name='inUse',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='machine',
            name='isBroken',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='machine',
            name='location',
            field=models.CharField(default='none', max_length=255),
        ),
    ]
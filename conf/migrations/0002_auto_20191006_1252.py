# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-06 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bugcollections',
            options={'ordering': ('bug_time',)},
        ),
        migrations.AlterField(
            model_name='bugcollections',
            name='bug_location',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='bugcollections',
            name='bug_type',
            field=models.CharField(default='', max_length=25),
        ),
    ]

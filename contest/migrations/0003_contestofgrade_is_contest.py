# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-15 03:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contest', '0002_auto_20191006_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestofgrade',
            name='is_contest',
            field=models.BooleanField(default=False, verbose_name='是否为创建成功的竞赛'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-26 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='type',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='公告类型'),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='created_by',
            field=models.CharField(default='Super Admin', max_length=12, verbose_name='创建者姓名'),
        ),
    ]
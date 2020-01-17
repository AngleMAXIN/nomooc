# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-23 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0004_auto_20191006_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='call_count',
            field=models.PositiveIntegerField(default=0, verbose_name='被竞赛引用次数'),
        ),
        migrations.AddField(
            model_name='problem',
            name='old_pro_dis_id',
            field=models.IntegerField(default=0, verbose_name='公有题库试题_id'),
        ),
    ]
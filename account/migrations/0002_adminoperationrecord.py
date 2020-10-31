# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2019-12-29 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminOperationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default=0, verbose_name='姓名')),
                ('u_type', models.CharField(default='', max_length=20, verbose_name='用户权限')),
                ('action_time', models.DateTimeField(auto_now_add=True, verbose_name='发生时间')),
                ('api', models.CharField(default='', max_length=255, verbose_name='请求api')),
                ('action', models.CharField(default='', max_length=7, verbose_name='动作')),
                ('location', models.CharField(default='', max_length=100, verbose_name='页面')),
            ],
            options={
                'db_table': 'admin_op_record',
            },
        ),
    ]

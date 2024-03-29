# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-19 03:47
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import utils.models
import utils.shortcuts


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('contest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', utils.models.MyCharField(db_index=True, default=utils.shortcuts.rand_str, max_length=32,
                                                    verbose_name='记录编号')),
                ('problem_id', models.IntegerField(default=0, verbose_name='试题id')),
                ('display_id', models.IntegerField(null=True, verbose_name='编号')),
                ('result', models.IntegerField(default=6, verbose_name='结果')),
                ('info', utils.models.MyJSONField(default=dict, verbose_name='判题详情')),
                ('language', utils.models.MyCharField(max_length=10, verbose_name='语言')),
                ('shared', models.BooleanField(default=False, verbose_name='')),
                ('length', models.PositiveSmallIntegerField(default=0, verbose_name='代码长度')),
                ('statistic_info', utils.models.MyJSONField(default=dict)),
                ('ip', utils.models.MyCharField(default='', max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('user_id', models.IntegerField(db_index=True, verbose_name='用户id')),
                ('real_name', models.CharField(default='', max_length=50, verbose_name='用户名')),
                ('code', models.TextField(verbose_name='提交代码')),
                ('contest',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contest.Contest',
                                   verbose_name='竞赛id')),
            ],
            options={
                'db_table': 'submission',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='TestSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_id', utils.models.MyCharField(db_index=True, default=utils.shortcuts.rand_str, max_length=32,
                                                    verbose_name='记录编号')),
                ('result', models.IntegerField(default=6, verbose_name='结果')),
                ('problem_id', models.IntegerField(default=0, verbose_name='试题编号')),
                ('contest_id', models.IntegerField(default=0, null=True, verbose_name='竞赛编号')),
                ('info', utils.models.MyJSONField(default=dict, verbose_name='判题详情')),
                ('language', utils.models.MyCharField(max_length=10, verbose_name='语言')),
                ('code', models.TextField(verbose_name='提交代码')),
                ('statistic_info', utils.models.MyJSONField(default=dict)),
                ('ip', utils.models.MyCharField(default='', max_length=20)),
            ],
            options={
                'db_table': 'test_submission',
            },
        ),
    ]

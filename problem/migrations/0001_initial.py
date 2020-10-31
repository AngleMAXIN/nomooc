# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-09-19 03:48
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import utils.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestProblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField(db_index=True, verbose_name='编号')),
                ('is_public', models.BooleanField(default=False, verbose_name='是否公开')),
                ('title', utils.models.MyCharField(default='题目标题', max_length=45)),
                ('description', utils.models.MyRichTextField(verbose_name='描述')),
                ('input_description', utils.models.MyRichTextField(verbose_name='输入描述')),
                ('output_description', utils.models.MyRichTextField(verbose_name='输出描述')),
                ('samples', utils.models.MyJSONField(verbose_name='例子')),
                ('test_case_id', models.CharField(default='', max_length=200, verbose_name='测试用例')),
                ('test_case_score', utils.models.MyJSONField(verbose_name='测试用例详情')),
                ('hint', utils.models.MyRichTextField(null=True, verbose_name='提示')),
                ('spj', models.BooleanField(default=False, verbose_name='是否为spj')),
                ('languages', utils.models.MyJSONField(verbose_name='支持语言')),
                ('template', utils.models.MyJSONField(default={}, verbose_name='模板')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_update_time', models.DateTimeField(null=True, verbose_name='最近修改时间')),
                ('time_limit', models.IntegerField(verbose_name='cpu时间限制')),
                ('memory_limit', models.IntegerField(verbose_name='内存限制')),
                ('rule_type', utils.models.MyCharField(default='ACM', max_length=3, verbose_name='比赛类型')),
                ('visible', models.BooleanField(default=True, verbose_name='是否可见')),
                ('difficulty', utils.models.MyCharField(default='', max_length=3, verbose_name='难度')),
                ('bank', models.SmallIntegerField(default=1, verbose_name='题库')),
                ('answer', utils.models.MyJSONField(default=[], verbose_name='答案')),
                ('total_score', models.IntegerField(default=0)),
                ('submission_number', models.IntegerField(default=0, verbose_name='提交次数')),
                ('accepted_number', models.IntegerField(default=0, verbose_name='通过次数')),
                ('statistic_info', utils.models.MyJSONField(default=dict)),
                ('test_cases', utils.models.MyJSONField(default=[], verbose_name='测试用例')),
                ('contest_id', models.PositiveIntegerField(default=0, verbose_name='竞赛id')),
                ('source',
                 models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                   verbose_name='来源')),
            ],
            options={
                'db_table': 'contest_problem',
            },
        ),
        migrations.CreateModel(
            name='ContestProblemBasketModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='用户id')),
                ('problem_basket', utils.models.MyJSONField(verbose_name='试题篮')),
            ],
            options={
                'db_table': 'problem_basket',
            },
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.IntegerField(db_index=True, verbose_name='编号')),
                ('is_public', models.BooleanField(default=False, verbose_name='是否公开')),
                ('title', utils.models.MyCharField(default='题目标题', max_length=45)),
                ('description', utils.models.MyRichTextField(verbose_name='描述')),
                ('input_description', utils.models.MyRichTextField(verbose_name='输入描述')),
                ('output_description', utils.models.MyRichTextField(verbose_name='输出描述')),
                ('samples', utils.models.MyJSONField(verbose_name='例子')),
                ('test_case_id', models.CharField(default='', max_length=200, verbose_name='测试用例')),
                ('test_case_score', utils.models.MyJSONField(verbose_name='测试用例详情')),
                ('hint', utils.models.MyRichTextField(null=True, verbose_name='提示')),
                ('spj', models.BooleanField(default=False, verbose_name='是否为spj')),
                ('languages', utils.models.MyJSONField(verbose_name='支持语言')),
                ('template', utils.models.MyJSONField(default={}, verbose_name='模板')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_update_time', models.DateTimeField(null=True, verbose_name='最近修改时间')),
                ('time_limit', models.IntegerField(verbose_name='cpu时间限制')),
                ('memory_limit', models.IntegerField(verbose_name='内存限制')),
                ('rule_type', utils.models.MyCharField(default='ACM', max_length=3, verbose_name='比赛类型')),
                ('visible', models.BooleanField(default=True, verbose_name='是否可见')),
                ('difficulty', utils.models.MyCharField(default='', max_length=3, verbose_name='难度')),
                ('bank', models.SmallIntegerField(default=1, verbose_name='题库')),
                ('answer', utils.models.MyJSONField(default=[], verbose_name='答案')),
                ('total_score', models.IntegerField(default=0)),
                ('submission_number', models.IntegerField(default=0, verbose_name='提交次数')),
                ('accepted_number', models.IntegerField(default=0, verbose_name='通过次数')),
                ('statistic_info', utils.models.MyJSONField(default=dict)),
                ('test_cases', utils.models.MyJSONField(default=[], verbose_name='测试用例')),
                ('old_pro_id', models.IntegerField(default=0, verbose_name='公有题库试题id')),
                ('source',
                 models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL,
                                   verbose_name='来源')),
            ],
            options={
                'db_table': 'problem',
            },
        ),
        migrations.CreateModel(
            name='ProblemTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25, verbose_name='名称')),
            ],
            options={
                'db_table': 'problem_tag',
            },
        ),
        migrations.AddField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(default='', to='problem.ProblemTag', verbose_name='标签'),
        ),
        migrations.AlterUniqueTogether(
            name='contestproblem',
            unique_together=set([('id', 'contest_id')]),
        ),
        migrations.AlterIndexTogether(
            name='contestproblem',
            index_together=set([('id', 'contest_id')]),
        ),
    ]

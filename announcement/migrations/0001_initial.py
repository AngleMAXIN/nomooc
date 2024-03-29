# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-10-23 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        # migrations.DeleteModel(
        #     name="Announcement"
        # ),
        migrations.CreateModel(

            name='Announcements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('content', utils.models.MyRichTextField()),
                ('created_by', models.CharField(default='Root', max_length=12, verbose_name='创建者姓名')),
                ('created_by_type', models.CharField(default='Super Admin', max_length=30, verbose_name='创建者身份')),
                ('created_by_id', models.IntegerField(default=0, verbose_name='创建者id')),
                ('last_update_time', models.DateTimeField(auto_now=True, verbose_name='上次修改时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('visible', models.BooleanField(default=True, verbose_name='是否可见')),
            ],
            options={
                'db_table': 'announcements',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', utils.models.MyJSONField(default={}, verbose_name='消息体')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(null=True, verbose_name='修改时间')),
                ('writer_id', models.IntegerField(default=0, verbose_name='消息创建者')),
                ('type', models.CharField(default='info', max_length=10, verbose_name='消息类型')),
                ('scene', models.IntegerField(default=1, verbose_name='消息场景')),
            ],
            options={
                'db_table': 'notify_message',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(default=0, verbose_name='消息接受者')),
                ('message_id', models.IntegerField(default=0, verbose_name='消息体id')),
                ('read_time', models.DateTimeField(null=True, verbose_name='读取时间')),
                ('is_read', models.BooleanField(default=False, verbose_name='是否读取')),
            ],
            options={
                'db_table': 'user_massage',
            },
        ),
        migrations.AlterIndexTogether(
            name='usermessage',
            index_together=set([('uid', 'message_id')]),
        ),
    ]

# Generated by Django 2.1.7 on 2020-07-08 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='up_time',
        ),
        migrations.AddField(
            model_name='likes',
            name='is_cancel',
            field=models.BooleanField(default=False, verbose_name='是否取消'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='点赞/点踩时间'),
        ),
    ]

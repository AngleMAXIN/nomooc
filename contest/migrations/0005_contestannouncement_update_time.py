# Generated by Django 2.1.7 on 2020-01-06 09:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0004_auto_20191026_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestannouncement',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 6, 9, 1, 31, 4623, tzinfo=utc)),
        ),
    ]

# Generated by Django 2.2 on 2019-05-07 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190430_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 7, 6, 43, 31, 50519)),
        ),
        migrations.AlterField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=1),
        ),
    ]

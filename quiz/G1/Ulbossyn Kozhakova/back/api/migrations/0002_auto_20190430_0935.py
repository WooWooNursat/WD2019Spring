# Generated by Django 2.2 on 2019-04-30 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 9, 35, 53, 326889)),
        ),
    ]
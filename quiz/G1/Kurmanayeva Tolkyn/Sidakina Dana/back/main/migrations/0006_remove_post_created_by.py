# Generated by Django 2.2.1 on 2019-05-06 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190506_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='created_by',
        ),
    ]
# Generated by Django 2.2.1 on 2019-05-06 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='loke_count',
            new_name='like_count',
        ),
    ]

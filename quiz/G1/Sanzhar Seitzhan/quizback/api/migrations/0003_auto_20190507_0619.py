# Generated by Django 2.1.7 on 2019-05-07 06:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190507_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=None, to=settings.AUTH_USER_MODEL),
        ),
    ]

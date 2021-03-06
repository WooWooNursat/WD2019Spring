# Generated by Django 2.0.13 on 2019-05-07 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20190506_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('phone', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='course',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Lecture',
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
    ]

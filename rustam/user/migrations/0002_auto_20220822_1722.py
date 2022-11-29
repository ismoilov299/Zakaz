# Generated by Django 3.2.6 on 2022-08-22 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='active_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 17, 22, 43, 259070), verbose_name='Дата подписки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 22, 17, 22, 43, 259070), verbose_name='Дата окончания'),
        ),
    ]

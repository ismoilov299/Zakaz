# Generated by Django 3.2.6 on 2022-08-22 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220822_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='active_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата подписки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата окончания'),
        ),
    ]
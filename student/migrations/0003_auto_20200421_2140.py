# Generated by Django 3.0.5 on 2020-04-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200421_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.CharField(max_length=100, verbose_name='概述'),
        ),
    ]

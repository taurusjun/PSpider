# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-19 21:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20191119_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='discount',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='fare',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='price',
            name='tax',
            field=models.FloatField(null=True),
        ),
    ]

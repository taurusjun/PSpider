# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-20 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_price_subid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='subid',
            field=models.TextField(),
        ),
    ]

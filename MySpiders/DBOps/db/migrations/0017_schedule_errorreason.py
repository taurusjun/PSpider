# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-21 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0016_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='errorReason',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
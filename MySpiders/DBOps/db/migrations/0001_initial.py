# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-19 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='airline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.TextField()),
                ('name', models.TextField()),
                ('isLCC', models.BooleanField(default=False)),
                ('alliance', models.TextField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'airline',
            },
        ),
        migrations.CreateModel(
            name='craft',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('widthLevel', models.TextField()),
                ('craftType', models.TextField()),
                ('minSeats', models.IntegerField()),
                ('maxSeats', models.IntegerField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'craft',
            },
        ),
        migrations.CreateModel(
            name='flight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dCityCode', models.TextField()),
                ('aCityCode', models.TextField()),
                ('dPortCode', models.TextField()),
                ('aPortCode', models.TextField()),
                ('dTime', models.BigIntegerField()),
                ('aTime', models.BigIntegerField()),
                ('flightNo', models.TextField()),
                ('flightFlag', models.TextField()),
                ('cabinClass', models.TextField()),
                ('luggageDirectStatus', models.TextField()),
                ('luggageDirectDesc', models.TextField()),
                ('luggageDirectTitle', models.TextField()),
                ('tripRefId', models.IntegerField()),
                ('airlineRefId', models.IntegerField()),
                ('craftRefId', models.IntegerField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'flight',
            },
        ),
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.TextField()),
                ('totalPrice', models.FloatField()),
                ('tax', models.FloatField()),
                ('fare', models.FloatField()),
                ('discount', models.FloatField()),
                ('flightRefId', models.IntegerField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'price',
            },
        ),
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('departureCityCode', models.TextField()),
                ('arrivalCityCode', models.TextField()),
                ('scheduleDate', models.DateField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='trip',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('departureCityCode', models.TextField()),
                ('arrivalCityCode', models.TextField()),
                ('departureTime', models.BigIntegerField()),
                ('arrivalTime', models.BigIntegerField()),
                ('cityStopList', models.TextField()),
                ('scheduleRefId', models.IntegerField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'trip',
            },
        ),
    ]
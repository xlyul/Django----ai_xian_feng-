# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainMustBuy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=128)),
                ('track_id', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_must_buy',
            },
        ),
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=128)),
                ('track_id', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_nav',
            },
        ),
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=128)),
                ('track_id', models.CharField(max_length=16)),
                ('img1', models.CharField(max_length=256)),
                ('long_name1', models.CharField(max_length=128)),
                ('price1', models.FloatField(default=0)),
                ('market_price1', models.FloatField(default=1)),
                ('img2', models.CharField(max_length=256)),
                ('long_name2', models.CharField(max_length=128)),
                ('price2', models.FloatField(default=0)),
                ('market_price2', models.FloatField(default=1)),
                ('img3', models.CharField(max_length=256)),
                ('long_name3', models.CharField(max_length=128)),
                ('price3', models.FloatField(default=0)),
                ('market_price3', models.FloatField(default=1)),
            ],
            options={
                'db_table': 'axf_mainshow',
            },
        ),
        migrations.CreateModel(
            name='MainWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=128)),
                ('track_id', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'axf_wheel',
            },
        ),
    ]

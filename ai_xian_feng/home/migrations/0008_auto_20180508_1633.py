# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 08:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180508_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='new_category_id',
            field=models.ForeignKey(default=models.CharField(max_length=16), on_delete=django.db.models.deletion.CASCADE, to='home.FoodType'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='category_id',
            field=models.CharField(max_length=16),
        ),
    ]

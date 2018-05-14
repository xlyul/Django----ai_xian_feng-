# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180508_1634'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goods',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='new_category_id',
        ),
        migrations.AddField(
            model_name='goods',
            name='new_category',
            field=models.ForeignKey(default=models.CharField(max_length=16), on_delete=django.db.models.deletion.CASCADE, to='home.FoodType'),
        ),
    ]
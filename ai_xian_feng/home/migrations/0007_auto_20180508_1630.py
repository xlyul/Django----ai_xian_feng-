# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 08:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_usermodel_user_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.FoodType'),
        ),
    ]

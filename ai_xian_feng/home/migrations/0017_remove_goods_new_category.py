# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20180508_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='new_category',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-08 08:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20180508_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='new_category',
        ),
    ]

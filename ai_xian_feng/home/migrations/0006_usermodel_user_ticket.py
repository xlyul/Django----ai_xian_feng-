# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-07 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20180507_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='user_ticket',
            field=models.CharField(max_length=256, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 07:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20161009_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

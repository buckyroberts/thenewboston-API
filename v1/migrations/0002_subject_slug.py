# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-24 22:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='slug',
            field=models.CharField(default='', max_length=64),
        ),
    ]

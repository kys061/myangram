# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-07 05:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20180207_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='images.Image'),
        ),
    ]

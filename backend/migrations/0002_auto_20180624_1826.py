# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures',
            name='last_used',
            field=models.DateTimeField(null=True),
        ),
    ]

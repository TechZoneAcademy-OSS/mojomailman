# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-05-29 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailusers', '0002_auto_20160529_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mojomailmanuser',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

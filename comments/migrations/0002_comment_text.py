# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-01 06:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]

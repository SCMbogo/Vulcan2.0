# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='slug',
            field=models.SlugField(blank=True, max_length=100),
        ),
    ]
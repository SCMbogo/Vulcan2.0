# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=b'documents')),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2021-12-24 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={'ordering': ['nombre']},
        ),
    ]
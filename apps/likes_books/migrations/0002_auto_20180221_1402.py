# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-21 14:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('likes_books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
        migrations.RemoveField(
            model_name='book',
            name='users',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
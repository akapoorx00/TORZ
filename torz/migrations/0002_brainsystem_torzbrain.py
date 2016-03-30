# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrainSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('knowledge', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TorzBrain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brain', models.CharField(max_length=32)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-30 19:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torz', '0005_auto_20160330_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLClicks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('number', models.CharField(default=0, max_length=4)),
            ],
        ),
        migrations.AlterField(
            model_name='brainsystem',
            name='knowledge',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='brainsystem',
            name='query',
            field=models.CharField(default=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='torzbrain',
            name='brain',
            field=models.CharField(max_length=200),
        ),
    ]
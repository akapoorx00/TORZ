# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-08 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torz', '0006_auto_20160330_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchClick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=600)),
            ],
        ),
    ]
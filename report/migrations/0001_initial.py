# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-12-20 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Performset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perform_id', models.IntegerField(unique=True)),
                ('perform_name', models.CharField(max_length=20)),
            ],
        ),
    ]

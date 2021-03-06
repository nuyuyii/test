# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-07 11:54
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', django.contrib.postgres.fields.jsonb.JSONField(default=[])),
                ('climdex', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('coordinates', django.contrib.postgres.fields.jsonb.JSONField(default=[])),
            ],
        ),
        migrations.CreateModel(
            name='Ts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]

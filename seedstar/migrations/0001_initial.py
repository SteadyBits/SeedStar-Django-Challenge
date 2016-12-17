# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30, blank=False)),
                ('lname', models.CharField(max_length=30, blank=False)),
                ('email_address', models.EmailField(max_length=50, blank=False, unique=True)),
            ],
        ),
    ]
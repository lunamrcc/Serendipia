# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiantes',
            name='Passwd',
            field=models.CharField(max_length=20),
        ),
    ]

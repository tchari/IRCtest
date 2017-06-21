# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 16:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IRC', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='assessor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
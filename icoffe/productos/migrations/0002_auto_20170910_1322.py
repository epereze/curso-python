# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-10 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='insumo',
            field=models.ManyToManyField(blank=True, to='productos.Insumo'),
        ),
    ]

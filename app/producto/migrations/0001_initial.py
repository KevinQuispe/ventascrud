# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 17:47
from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=80)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
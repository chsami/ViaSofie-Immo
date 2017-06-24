# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-30 14:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20170330_0952'),
    ]

    operations = [
        migrations.CreateModel(
            name='PandEPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naam', models.CharField(max_length=128)),
                ('waarde', models.CharField(max_length=128)),
                ('pand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Pand')),
            ],
        ),
    ]

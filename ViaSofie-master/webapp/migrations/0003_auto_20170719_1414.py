# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-19 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20170719_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='PandPandEPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='pandepc',
            name='pand',
        ),
        migrations.AddField(
            model_name='pandpandepc',
            name='epc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.PandEPC'),
        ),
        migrations.AddField(
            model_name='pandpandepc',
            name='pand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Pand'),
        ),
    ]

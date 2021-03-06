# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-10 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_id', models.CharField(max_length=100)),
                ('url', models.URLField(max_length=100)),
                ('filename', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='downloader.Audio')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-11 05:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('downloader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_text', models.CharField(default='', max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='audio',
        ),
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

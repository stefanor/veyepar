# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-14 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160710_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mark',
            options={'ordering': ['click']},
        ),
        migrations.AddField(
            model_name='show',
            name='youtube_playlist_id',
            field=models.CharField(blank=True, help_text='Playlist ID for YouTube', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='channelcopy',
            field=models.CharField(blank=True, help_text='m=mono, 01=copy left to right, 10=right to left, 00=ignore.', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='episode',
            name='edit_key',
            field=models.CharField(blank=True, default='37973352', help_text='key to allow unauthenticated users to edit this item.', max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(default='smetana', help_text='room name', max_length=135),
        ),
    ]

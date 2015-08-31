# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=datetime.datetime(2015, 8, 31, 8, 1, 3, 936561, tzinfo=utc))),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]

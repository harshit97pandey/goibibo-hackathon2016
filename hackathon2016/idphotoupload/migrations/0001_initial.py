# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckInPhotoDB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Userid', models.IntegerField()),
                ('AWSPhotoUrl', models.CharField(max_length=300)),
                ('Email', models.CharField(max_length=60)),
                ('Mobile', models.CharField(max_length=20)),
                ('DateCreated', models.DateTimeField(default=datetime.datetime(2016, 10, 14, 16, 10, 22, 722109), null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

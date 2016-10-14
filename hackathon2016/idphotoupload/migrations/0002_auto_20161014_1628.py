# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('idphotoupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkinphotodb',
            name='DateCreated',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 14, 16, 28, 13, 935813), null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkinphotodb',
            name='Email',
            field=models.CharField(default=b'', max_length=60, null=True, db_index=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkinphotodb',
            name='Mobile',
            field=models.CharField(default=b'', max_length=20, null=True, db_index=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='checkinphotodb',
            name='Userid',
            field=models.IntegerField(db_index=True),
            preserve_default=True,
        ),
    ]

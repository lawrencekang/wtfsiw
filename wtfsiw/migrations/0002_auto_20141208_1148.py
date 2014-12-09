# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wtfsiw', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='home_address',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='home_location',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='category',
            field=models.IntegerField(default=None, choices=[(0, b'Article'), (1, b'Video'), (2, b'Music')]),
        ),
    ]

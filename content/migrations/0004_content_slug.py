# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20150809_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]

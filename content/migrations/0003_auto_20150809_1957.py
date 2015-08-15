# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_content_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.IntegerField(default=None, choices=[(0, b'Article'), (1, b'Video'), (2, b'Music'), (3, b'Book')]),
        ),
        migrations.AddField(
            model_name='collection',
            name='contents',
            field=models.ManyToManyField(to='content.Content'),
        ),
    ]

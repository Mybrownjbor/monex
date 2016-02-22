# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0004_auto_20160222_0318'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitionrank',
            name='fee',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competitionrank',
            name='first',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competitionrank',
            name='second',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='competitionrank',
            name='third',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0006_auto_20160222_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitionrank',
            name='shagnal',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]

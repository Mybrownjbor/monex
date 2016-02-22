# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bank',
            field=models.ForeignKey(default=1, verbose_name=b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba:', to='user.Bank'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0005_auto_20160222_0339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competitionrank',
            name='first',
        ),
        migrations.RemoveField(
            model_name='competitionrank',
            name='second',
        ),
        migrations.RemoveField(
            model_name='competitionrank',
            name='third',
        ),
        migrations.AlterField(
            model_name='competitionrank',
            name='fee',
            field=models.IntegerField(verbose_name='\u0421\u0443\u0443\u0440\u044c \u0445\u0443\u0440\u0430\u0430\u043c\u0436:'),
        ),
        migrations.AlterField(
            model_name='competitionrank',
            name='name',
            field=models.CharField(max_length=100, verbose_name='\u041d\u044d\u0440:'),
        ),
    ]

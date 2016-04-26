# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(verbose_name='\u042d\u0445\u043b\u044d\u0445 \u043e\u0433\u043d\u043e\u043e')),
                ('end', models.DateTimeField(verbose_name='\u0414\u0443\u0443\u0441\u0430\u0445 \u043e\u0433\u043d\u043e\u043e')),
                ('status', models.BooleanField(default=False)),
                ('competition_status', models.CharField(default=b'0', max_length=10, verbose_name=b'\xd0\xa2\xd3\xa9\xd0\xbb\xd3\xa9\xd0\xb2', choices=[(b'0', '\u0411\u04af\u0440\u0442\u0433\u044d\u043b \u044d\u0445\u044d\u043b\u0441\u044d\u043d'), (b'1', '\u042d\u0445\u044d\u043b\u0441\u044d\u043d'), (b'2', '\u0414\u0443\u0443\u0441\u0441\u0430\u043d')])),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionRank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u044d\u0440')),
                ('fee', models.IntegerField(verbose_name='\u0421\u0443\u0443\u0440\u044c \u0445\u0443\u0440\u0430\u0430\u043c\u0436')),
                ('shagnal', models.TextField(verbose_name='\u0428\u0430\u0433\u043d\u0430\u043b\u044b\u043d \u0441\u0430\u043d')),
            ],
        ),
        migrations.AddField(
            model_name='competition',
            name='rank',
            field=models.ForeignKey(verbose_name='\u0410\u043d\u0433\u0438\u043b\u0430\u043b', to='competition.CompetitionRank'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=2, choices=[(b'0', '\u0411\u0438\u0434\u043d\u0438\u0439 \u0442\u0443\u0445\u0430\u0439'), (b'0', '\u041c\u044d\u0434\u044d\u044d\u043b\u044d\u043b'), (b'0', '\u0421\u0443\u0434\u0430\u043b\u0433\u0430\u0430'), (b'0', '\u0421\u0443\u0440\u0433\u0430\u043b\u0442'), (b'0', '\u0411\u0430\u0433\u0446')])),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('view', models.SmallIntegerField(default=0)),
                ('created_by', models.ForeignKey(to='manager.Manager')),
            ],
        ),
    ]

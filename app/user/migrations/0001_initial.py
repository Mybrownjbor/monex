# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=40, verbose_name='\u041d\u044d\u0440:')),
                ('lastname', models.CharField(max_length=40, verbose_name='\u041e\u0432\u043e\u0433:')),
                ('register', models.CharField(unique=True, max_length=10, verbose_name='\u0420\u0435\u0433\u0438\u0441\u0442\u0435\u0440:')),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='\u042d-\u043c\u044d\u0439\u043b:')),
                ('phone', models.IntegerField(verbose_name='\u0423\u0442\u0430\u0441:')),
                ('account', models.IntegerField(verbose_name=b'\xd0\x94\xd0\xb0\xd0\xbd\xd1\x81\xd0\xbd\xd0\xb8\xd0\xb9 \xd0\xb4\xd1\x83\xd0\xb3\xd0\xb0\xd0\xb0\xd1\x80:')),
                ('password', models.CharField(max_length=15, verbose_name='\u041d\u0443\u0443\u0446 \u04af\u0433:')),
                ('bank', models.ForeignKey(verbose_name=b'\xd0\x91\xd0\xb0\xd0\xbd\xd0\xba:', to='user.Bank')),
            ],
        ),
    ]

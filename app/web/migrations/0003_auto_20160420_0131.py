# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_medee'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedeeAngilal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('angilal', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterModelOptions(
            name='medee',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='medee',
            name='category',
            field=models.ForeignKey(to='web.MedeeAngilal'),
        ),
    ]

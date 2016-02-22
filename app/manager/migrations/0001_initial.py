# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupManagerRoleJoin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('group_manager_role_join', models.ManyToManyField(to='manager.GroupManagerRoleJoin')),
            ],
        ),
        migrations.CreateModel(
            name='ManagerRoleJoin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='manager',
            name='manager_role_join',
            field=models.ManyToManyField(to='manager.ManagerRoleJoin'),
        ),
        migrations.AddField(
            model_name='groupmanagerrolejoin',
            name='manager_role_join',
            field=models.ManyToManyField(to='manager.ManagerRoleJoin'),
        ),
    ]

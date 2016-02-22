# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='username',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='groupmanagerrolejoin',
            name='manager_role_join',
            field=models.ManyToManyField(to='manager.ManagerRoleJoin', blank=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='group_manager_role_join',
            field=models.ManyToManyField(to='manager.GroupManagerRoleJoin', blank=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='manager_role_join',
            field=models.ManyToManyField(to='manager.ManagerRoleJoin', blank=True),
        ),
    ]

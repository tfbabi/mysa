# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sphinx',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('sshport', models.CharField(max_length=100)),
                ('indexerbin', models.CharField(max_length=200)),
                ('conf', models.CharField(max_length=200)),
            ],
        ),
    ]

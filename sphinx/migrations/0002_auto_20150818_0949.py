# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sphinx', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sphinx',
            new_name='Sphinxinfo',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='amount',
            new_name='quantity',
        ),
    ]

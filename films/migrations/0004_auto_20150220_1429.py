# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]

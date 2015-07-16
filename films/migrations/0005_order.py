# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_auto_20150220_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(to='films.Film')),
            ],
            options={
                'verbose_name': 'Заказ',
                'db_table': 'order',
                'verbose_name_plural': 'Заказы',
            },
            bases=(models.Model,),
        ),
    ]

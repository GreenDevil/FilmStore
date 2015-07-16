# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20150219_1626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
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

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comments_text', models.TextField(verbose_name='Текст коментария')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
                'db_table': 'comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Название фильма', max_length=100)),
                ('description', models.TextField(verbose_name='Описание')),
                ('value', models.IntegerField(verbose_name='Цена')),
                ('amount', models.IntegerField(verbose_name='Количество', default=0)),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'db_table': 'film',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comments',
            name='comments_film',
            field=models.ForeignKey(to='films.Film'),
            preserve_default=True,
        ),
    ]

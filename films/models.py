#-*- coding utf-8 -*-
from django.db import models

# Create your models here.
class Film(models.Model):
    class Meta:
        db_table = 'film'
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'

    title = models.CharField(max_length=100, verbose_name='Название фильма')
    description = models.TextField(verbose_name='Описание')
    value = models.IntegerField(verbose_name='Цена')
    quantity = models.IntegerField(default=0, verbose_name='Количество')

    def __unicode__(self):
        return self.title


class Comments(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    comments_text = models.TextField(verbose_name='Текст коментария')
    comments_film = models.ForeignKey(Film)

class Order(models.Model):
    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    order = models.ForeignKey(Film)
    quantity = models.IntegerField(verbose_name='Количество')

    def title(self):
        return self.order.title

    def value(self):
        return self.order.value

    def total(self):
        return self.quantity * self.order.value
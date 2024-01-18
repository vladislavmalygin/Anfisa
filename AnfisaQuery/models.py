from django.db import models
from django import forms


class AnfisaDatabase(models.Model):
    name = models.CharField('Имя', max_length=50)
    city = models.CharField('Город', max_length=50)

    def __str__(self):
        return f'{self.name}, {self.city}'

    def __repr__(self):
        return f'{self.name}, {self.city}'

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'


class TimeZones(models.Model):
    city = models.CharField('Город', max_length=50, default='SOME STRING')
    timezone = models.IntegerField('Разница времени с UTC')

    def __str__(self):
        return self.city, self.timezone


class Meta:
    verbose_name: str = 'Город'
    verbose_name = 'Разница времени с UTC'
    verbose_name_plural = 'Значения разницы во времени с UTC'


class QueryDatabase(models.Model):
    query = models.TextField('Запрос', max_length=200, )

    def __str__(self):
        return f'{self.query}'

    def __repr__(self):
        return f'{self.query}'


class Meta:
    verbose_name = 'Запрос'
    verbose_name_plural = 'Запросы'


class AnswerDatabase(models.Model):
    answer = models.TextField()

    def __str__(self):
        return f'{self.answer}'

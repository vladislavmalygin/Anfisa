from django.db import models

class AnfisaDatabase(models.Model):
    name = models.CharField('Имя',max_length=50)
    city = models.CharField('Город',max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'

class TimeZones(models.Model):
    city = models.CharField('Город',max_length=50)
    timezone = models.IntegerField('Разница времени с UTC')






    def ___str___(self):
        return self.city, self.timezone

    class Meta:
        verbose_name: str = 'Город'
        verbose_name = 'Разница времени с UTC'
        verbose_name_plural = 'Значения разницы во времени с UTC'


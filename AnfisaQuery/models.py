from django.db import models

class AnfisaDatabase(models.Model):
    name = models.CharField('Имя',max_length=50)
    city = models.CharField('Город',max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Имя'
        verbose_name_plural = 'Имена'

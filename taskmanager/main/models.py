from django.db import models


class Task(models.Model):
    title = models.CharField('Названия', max_length=64)
    task = models.TextField('Описания')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачi'

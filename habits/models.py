import datetime

from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """
    Класс модели Habits.
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Создатель', **NULLABLE)
    action = models.CharField(max_length=200, verbose_name='Действие')
    place = models.CharField(max_length=200, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    date_start = models.DateField(verbose_name='Дата старта', default=datetime.date.today())
    pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', verbose_name='Связанная привычка', on_delete=models.SET_NULL, **NULLABLE)
    period = models.PositiveIntegerField(default=1, verbose_name='Периодичность привычки')
    reward = models.CharField(max_length=300, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveIntegerField(verbose_name='Время выполнения', **NULLABLE)
    is_public = models.BooleanField(default=True, verbose_name='Признак публикации')

    def __str__(self):
        """
        Строковое представление модели Habit.
        """
        return f'{self.action} - {self.time} - {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

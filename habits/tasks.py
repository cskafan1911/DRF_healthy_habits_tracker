from _datetime import datetime, timedelta

import pytz
import requests

from celery import shared_task
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.utils import timezone

from habits.models import Habit
from habits.services import create_telegram_message


@shared_task
def send_message_telegram():
    """
    Функция отправляет напоминание с привычкой в телеграм. Сообщение отправляется за 5 минут до старта.
    """
    url = 'https://api.telegram.org/bot'
    token = settings.TELEGRAM_TOKEN

    time_now = timezone.localtime()
    time = (time_now + relativedelta(minutes=5)).strftime('%H:%M')
    date_now = datetime.now().date().strftime('%Y-%m-%d')
    habits = Habit.objects.filter(time=time, pleasant_habit=False, date_start=date_now)

    if habits:
        for habit in habits:
            requests.post(
                url=f'{url}{token}/sendMessage',
                data={
                    'chat_id': habit.user.telegram_id,
                    'text': create_telegram_message(habit)
                }
            )
            habit.date_start += timedelta(days=habit.period)
            habit.save()

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):
    """
    Класс тестов для приложения habits.
    """

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test1@mail.ru',
            password='qwerty',
            telegram_id=1234
        )

        self.user_2 = User.objects.create(
            email='test100@mail.ru',
            password='qwerty',
            telegram_id=1234
        )

        self.habit_1 = Habit.objects.create(
            id=10,
            user=self.user,
            action='Пробежка',
            place='Школьный стадион',
            time='08:00:00',
            date_start='2024-03-12',
            pleasant_habit=False,
            period=1,
            time_to_complete=120,
            is_public=True,
        )

        self.habit_2 = Habit.objects.create(
            id=20,
            user=self.user,
            action='Выпить протеиновый коктейль',
            place='Дом',
            time='08:30:00',
            date_start='2024-03-12',
            pleasant_habit=True,
            reward='Съесть банан',
            period=1,
            time_to_complete=120,
            is_public=True,
        )

    def test_create_habit(self):
        """
        Тестирование создания полезной привычки.
        """
        self.client.force_authenticate(user=self.user)

        data = {
            'action': self.habit_1.action,
            'place': self.habit_1.place,
            'time': self.habit_1.time,
            'date_start': self.habit_1.date_start,
            'related_habit': self.habit_2.id,
            'pleasant_habit': self.habit_1.pleasant_habit,
            'period': self.habit_1.period,
            'is_public': self.habit_1.is_public

        }

        response = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_pleasant_habit(self):
        """
        Тестирование создания приятной привычки.
        """
        self.client.force_authenticate(user=self.user)

        data = {
            'action': self.habit_2.action,
            'place': self.habit_2.place,
            'time': self.habit_2.time,
            'date_start': self.habit_2.date_start,
            'pleasant_habit': self.habit_2.pleasant_habit,
            'period': self.habit_2.period,
            'is_public': self.habit_2.is_public

        }

        response = self.client.post(
            reverse('habits:habit_create'),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habit(self):
        """
        Тестирование просмотра привычек пользователя.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.get(
            reverse('habits:user_habits_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_list_habit_is_public(self):
        """
        Тестирование просмотра опубликованных привычек.
        """

        response = self.client.get(
            reverse('habits:is_public_habits_list')
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_pleasant_habit(self):
        """
        Тестирование редактирования привычки.
        """
        self.client.force_authenticate(user=self.user)

        data = {
            'action': 'test',
            'place': 'test',
            'time': '08:00:00',
            'period': self.habit_2.period,
            'is_public': self.habit_2.is_public

        }

        response = self.client.put(
            reverse('habits:habit_update', args=[self.habit_1.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_pleasant_habit_not_user(self):
        """
        Тестирование запрета редактирования привычки другим пользователем.
        """
        self.client.force_authenticate(user=self.user_2)

        data = {
            'action': 'test2',
            'place': 'test2',
            'time': '08:00:00',
            'period': self.habit_2.period,
            'is_public': self.habit_2.is_public

        }

        response = self.client.put(
            reverse('habits:habit_update', args=[self.habit_1.id]),
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_delete_habit(self):
        """
        Тестирование удаления привычки.
        """
        self.client.force_authenticate(user=self.user)

        response = self.client.delete(
            reverse('habits:habit_delete', args=[self.habit_1.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_delete_habit_not_user(self):
        """
        Тестирование удаления привычки другим пользователем.
        """
        self.client.force_authenticate(user=self.user_2)

        response = self.client.delete(
            reverse('habits:habit_delete', args=[self.habit_1.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

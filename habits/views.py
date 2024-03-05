from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.permissions import IsUserHabit
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Класс для создания привычки.
    """

    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """
        Метод привязывает пользователя и созданную им привычку.
        """
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitUserListAPIView(generics.ListAPIView):
    """
    Класс для просмотра списка привычек текущего пользователя.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUserHabit]

    def get_queryset(self):
        """
        Метод получает список привычек пользователя.
        """
        queryset = Habit.objects.filter(user=self.request.user)

        return queryset


class HabitIsPublicListAPIView(generics.ListAPIView):
    """
    Класс для просмотра публичных привычек.
    """

    serializer_class = HabitSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        Метод получает список привычек разрешенных для публикации.
        """
        queryset = Habit.objects.filter(is_public=True)

        return queryset


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Класс для изменения информации о привычке.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUserHabit]


class HabitDeleteAPIView(generics.DestroyAPIView):
    """
    Класс для удаления привычки.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUserHabit]

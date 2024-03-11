from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginators import HabitsPaginator
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
    pagination_class = HabitsPaginator

    def get_queryset(self):
        """
        Метод получает список привычек пользователя.
        """
        queryset = Habit.objects.filter(user=self.request.user)

        return queryset.order_by('id')


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

        return queryset.order_by('id')


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Класс для изменения информации о привычке.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUserHabit]

    def perform_update(self, serializer):
        """
        Метод для обновления привычек.
        """
        update_habit = serializer.save()
        update_habit.user = self.request.user

        if update_habit.related_habit:
            update_habit.reward = None
        if update_habit.pleasant_habit:
            update_habit.related_habit = None

        update_habit.save()


class HabitDeleteAPIView(generics.DestroyAPIView):
    """
    Класс для удаления привычки.
    """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsUserHabit]

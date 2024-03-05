from rest_framework import serializers

from habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Habit.
    """

    class Meta:
        model = Habit
        fields = '__all__'

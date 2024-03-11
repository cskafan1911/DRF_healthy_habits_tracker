from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitsValidator


class HabitSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Habit.
    """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitsValidator(field=['related_habit', 'reward'])]

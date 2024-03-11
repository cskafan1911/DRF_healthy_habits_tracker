from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitsValidator, RelatedHabitValidator, PleasantHabitValidator, TimeCompleteValidator, \
    PeriodValidator


class HabitSerializer(serializers.ModelSerializer):
    """
    Класс сериализатор для модели Habit.
    """

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            HabitsValidator(field=['related_habit', 'reward']),
            RelatedHabitValidator(field=['related_habit']),
            PleasantHabitValidator(field=['pleasant_habit', 'related_habit', 'reward']),
            TimeCompleteValidator(field=['time_to_complete']),
            PeriodValidator(field=['period'])
        ]

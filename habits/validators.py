from rest_framework import serializers


class HabitsValidator:
    """
    Класс валидатор для проверки заполнения полей Habit.
    """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        related_habit = value.get('related_habit')
        reward = value.get('reward')
        if related_habit is not None and reward is not None:
            raise serializers.ValidationError(
                "В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. "
                "Можно заполнить только одно из двух полей.")

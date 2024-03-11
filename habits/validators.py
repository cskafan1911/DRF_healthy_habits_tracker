from rest_framework import serializers


class HabitsValidatorMixin:
    """
    Класс Mixin для валидаторов модели Habit.
    """

    def __init__(self, field):
        self.field = field


class HabitsValidator(HabitsValidatorMixin):
    """
    Класс валидатор для проверки заполнения полей Habit.
    """

    def __call__(self, value):
        related_habit = dict(value).get('related_habit')
        reward = dict(value).get('reward')
        if related_habit is not None and reward is not None:
            raise serializers.ValidationError(
                'В модели не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. '
                'Можно заполнить только одно из двух полей.')


class RelatedHabitValidator(HabitsValidatorMixin):
    """
    Класс валидатор для проверки полей related_habit и pleasant_habit. Связанная привычка (related_habit) должна иметь
    признак приятной привычки (pleasant_habit).
    """

    def __call__(self, value):
        related_habit = value.get('related_habit')

        if related_habit:
            if not related_habit.pleasant_habit:
                raise serializers.ValidationError(
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки.')


class PleasantHabitValidator(HabitsValidatorMixin):
    """
    Класс валидатор для проверки приятной привычки (pleasant_habit). У приятной привычки (pleasant_habit=True) не должно
    быть вознаграждения (reward) или связанной привычки(related_habit).
    """

    def __call__(self, value):
        pleasant_habit = dict(value).get('pleasant_habit')
        related_habit = dict(value).get('related_habit')
        reward = dict(value).get('reward')

        if pleasant_habit:
            if reward is not None or related_habit is not None:
                raise serializers.ValidationError(
                    'У приятной привычки не может быть вознаграждения или связанной привычки.')


class TimeCompleteValidator(HabitsValidatorMixin):
    """
    Класс валидатор для проверки времени выполнения привычки.
    """

    def __call__(self, value):
        time = dict(value).get('time_to_complete')
        if time:
            if int(time) > 120:
                raise serializers.ValidationError('Время выполнения должно быть не больше 120 секунд.')


class PeriodValidator(HabitsValidatorMixin):
    """
    Класс валидатор для проверки периодичности выполнения привычки.
    """

    def __call__(self, value):
        period = dict(value).get('period')
        if int(period) > 7:
            raise serializers.ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')

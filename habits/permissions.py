from rest_framework import permissions


class IsUserHabit(permissions.BasePermission):
    """
    Класс прав доступа для создателя привычки.
    """

    message = 'Можно просматривать свои привычки или публичные привычки'

    def has_object_permission(self, request, view, obj):
        """
        Метод для проверки, является ли пользователь создателем привычки.
        """
        return obj.user == request.user

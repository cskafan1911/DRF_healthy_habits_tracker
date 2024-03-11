from rest_framework import permissions


class IsUser(permissions.BasePermission):
    """
    Класс прав доступа для просмотра и редактирования профиля пользователя.
    """

    message = 'Вы не можете просматривать, изменять и удалять информацию о других пользователях'

    def has_object_permission(self, request, view, obj):
        """
        Метод для проверки, является ли пользователь создателем привычки.
        """
        return obj == request.user

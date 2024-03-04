from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserListAPIView(generics.ListAPIView):
    """
    Класс для просмотра списка пользователей.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Класс для создания пользователя.
    """

    serializer_class = UserSerializer

    def perform_create(self, serializer):
        """
        Метод сохраняет нового пользователя и шифрует его пароль.
        """
        new_user = serializer.save()
        password = serializer.data["password"]
        new_user.set_password(password)
        new_user.save()


class UserDetailAPIView(generics.RetrieveAPIView):
    """
    Класс для просмотра данных пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    Класс для редактирования пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        """
        Метод сохраняет изменения профиля пользователя.
        """
        change_user = serializer.save()
        password = serializer.data['password']
        change_user.set_password(password)
        change_user.save()


class UserDeleteAPIView(generics.DestroyAPIView):
    """
    Класс для удаления пользователя.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

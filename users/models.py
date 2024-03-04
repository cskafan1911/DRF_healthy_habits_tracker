from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Класс модели User.
    """

    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150, verbose_name='Имя пользователя', blank=True, null=True)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия пользователя', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/', verbose_name='User Avatar', blank=True, null=True)
    city = models.CharField(max_length=150, verbose_name='Город', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

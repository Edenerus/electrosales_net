from django.db import models
from django.contrib.auth.models import AbstractUser

from network.models import Provider


class User(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    company = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True,
                                verbose_name='Компания', related_name='staff')

    REQUIRED_FIELDS = ['email',
                       'username'
                       'first_name',
                       'last_name',
                       'password']

    def __str__(self):
        return self.username

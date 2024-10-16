from django.db import models
from django.contrib.auth.models import AbstractUser

from users.services import NULLABLE


class User(AbstractUser):
    """Модель пользователя"""

    username = models.CharField(max_length=15, verbose_name="Имя пользователя", unique=True)
    email = models.EmailField(verbose_name="Email", unique=True)
    phone_number = models.CharField(
        max_length=25, verbose_name="Номер телефона", **NULLABLE
    )
    image = models.ImageField(
        upload_to="media/users/avatar/", verbose_name="Аватарка", **NULLABLE
    )
    token_for_password = models.CharField(
        max_length=100, verbose_name="Токен сброса пароля", **NULLABLE
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username

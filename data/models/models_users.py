from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    username = models.CharField(max_length=150, verbose_name="Имя пользователя")
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d", blank=True)
    id = models.AutoField(primary_key=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
from django.db import models
from django.contrib.auth.models import AbstractUser

class Profile(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/%Y/%m/%d", blank=True, null=True, verbose_name="Аватар")

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.html import strip_tags


class CastomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)


class Profile(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    username = models.CharField(max_length=150, verbose_name="Имя пользователя")
    avatar = models.ImageField(
        upload_to="avatars/%Y/%m/%d", blank=True, null=True, verbose_name="Аватар"
    )
    id = models.AutoField(primary_key=True)

    user = CastomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    def __str__(self):
        return self.email

    def clean(self):
        for field in [
            "avatar",
        ]:
            value = getattr(self, field)
            if value:
                setattr(self, field, strip_tags(value))

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth import get_user_model, authenticate
from django.utils.html import strip_tags
from django.core.validators import RegexValidator
from .models import Profile


class CustomProfileCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "email_form", "placeholder": "Email"}),
        label="Электронная почта",
    )
    username = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(
            attrs={"class": "username_form", "placeholder": "Имя пользователя"}
        ),
        label="Имя пользователя",
        validators=[
            RegexValidator(
                regex=r"^[\w.@+-]+$",
                message="Имя пользователя может содержать только буквы, цифры и символы @/./+/-/_",
            ),
        ],
    )

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "password_form", "placeholder": "Пароль"}
        ),
        label="Пароль",
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "password_form", "placeholder": "Подтверждение пароля"}
        ),
        label="Подтверждение пароля",
    )

    avatar = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": "avatar_form", "placeholder": "Аватар"}),
        label="Аватар",
    )

    class Meta:
        model = Profile
        fields = ("email", "username", "password1", "password2", "avatar")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Profile.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже зарегистрирован.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if Profile.objects.filter(username=username).exists():
            raise forms.ValidationError("Такой username уже существует.")
        return username
    

    def save(self, commit = True):
        return super().save(commit = commit)
        

class CustomProfileAuthenticationForm(AuthenticationForm):
    email = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "email_form", "placeholder": "Электронная почта"}),
        label="Электронная почта",
    )
    
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "password_form", "placeholder": "Пароль"}
        ),
        label="Пароль",
    )


    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            self.user_cache = authenticate(self.request, username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    "Пожалуйста, введите правильный username и пароль."
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError("Этот аккаунт не активен.")
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data
    

class CustomProfileUptadeForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "email_form", "placeholder": "Email"}),
        label="Электронная почта",
    )
    username = forms.CharField(
        required=True,
        max_length=150,
        widget=forms.TextInput(attrs={"class": "username_form", "placeholder": "Имя пользователя" }),
        label="Имя пользователя",
    )

    class Meta:
        model = Profile
        fields = ("email", "username")
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and Profile.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Этот email уже зарегистрирован.")
        return email
              

from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "title_form", "placeholder": "Название рецепта"}),
        label="Название рецепта",
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"class": "description_form", "placeholder": "Опишите рецепт здесь..."}),
        label="Описание рецепта",
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={"class": "category_form"}),
        label="Категория",
        required=True,
        empty_label=None,
    )
    ingredients = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"class": "ingredients_form", "placeholder": "Ингредиенты..."}),
        label="Ингредиенты",
    )
    instructions = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={"class": "instructions_form", "placeholder": "Инструкции..."}),
        label="Инструкции",
    )
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"class": "image_form"}),
        label="Изображение",
    )

    class Meta:
        model = Post
        fields = ['title', 'description', 'category', 'ingredients', 'instructions', 'image']
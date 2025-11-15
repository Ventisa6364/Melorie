from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(
        max_length=10,
        choices=[
            ("BK", "Завтрак"),
            ("LN", "Обед"),
            ("DN", "Ужин"),
            ("DS", "Десерт"),
            ("SN", "Закуска"),
            ("DR", "Напиток"),
        ],
    )
    ingredients = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "title",
        ]
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"


class Post(Recipe):
    author = models.CharField(max_length=50)
    title = Recipe.title
    category = Recipe.category
    recipe_ingredients = Recipe.ingredients
    recipe_instructions = Recipe.instructions
    published_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=100)
    image = models.ImageField(upload_to="posts/%Y/%m/%d", blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField('users.Profile', related_name='liked_posts', blank=True)
    saves = models.ManyToManyField('users.Profile', related_name='saved_posts', blank=True)

    def total_likes_post(self):
        return self.likes.count()
    
    def total_saves_post(self):
        return self.saves.count()

    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        ordering = [
            "-published_at",
        ]
        verbose_name = "Пост"
        verbose_name_plural = "Посты"



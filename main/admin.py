from django.contrib import admin
from .models import Recipe, Post

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'description', 'ingredients')
    list_filter = ('category',)
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')
    search_fields = ('title', 'author', 'recipe_ingredients')
    list_filter = ('published_at', 'author')
    prepopulated_fields = {'slug': ('title',)}


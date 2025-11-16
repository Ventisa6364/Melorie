from django.contrib import admin
from .models import Post
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', )
    search_fields = ('title', 'author', 'recipe_ingredients')
    list_filter = ('title', 'published_at', 'author')
    prepopulated_fields = {'slug': ('title',)}




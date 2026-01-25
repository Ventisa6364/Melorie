from django.contrib import admin
from data.models.models_posts import Post
from data.models.models_users import Profile
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', )
    search_fields = ('title', 'author', 'recipe_ingredients')
    list_filter = ('title', 'published_at', 'author')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email',)
    search_fields = ('username',)
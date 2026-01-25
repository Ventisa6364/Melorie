from presentation.view import views_posts
from django.urls import path

app_name = 'posts'

urlpatterns = [
    path('', views_posts.home_page, name='home_page'),
    path('posts/<slug:post_slug>/', views_posts.post_detail, name='post_detail'),
    path('posts/post_create', views_posts.post_create, name='post_create'),
    path('posts/<slug:post_slug>/like/', views_posts.like_post, name='like_post'),
    path('posts/<slug:post_slug>/save/', views_posts.save_post, name='save_post'),
]
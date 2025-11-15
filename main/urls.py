from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('posts/<slug:post_slug>/', views.post_detail, name='post_detail'),
    path('posts/post_create', views.post_create, name='post_create'),
    path('posts/<slug:post_slug>/like/', views.like_post, name='like_post'),
    path('posts/<slug:post_slug>/save/', views.save_post, name='save_post'),
]

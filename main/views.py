from django.shortcuts import render, get_object_or_404
from .models import Recipe, Post


def home_page(request, post_slug=None):
    categories = Post.objects.values_list('category', flat=True).distinct()
    posts = Post.objects.all()

    if post_slug:
        post = get_object_or_404(Post, slug=post_slug)
    
    return render(request, 'main/base.html', {'posts': posts, 'categories': categories})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, 'main/post/post_detail.html', {'post': post})

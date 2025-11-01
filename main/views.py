from django.shortcuts import render, get_object_or_404
from .models import Post


def home_page(request):
    posts = Post.objects.all()
    
    return render(request, 'main/base.html', {'posts': posts,})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, 'main/post/post_detail.html', {'post': post,})

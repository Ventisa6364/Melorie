from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post


def home_page(request):
    posts = Post.objects.all()
    
    return render(request, 'main/base.html', {'posts': posts,})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    total_likes = post.total_likes_post()
    total_saves = post.total_saves_post()
    return render(request, 'main/post/post_detail.html', {'post': post,})


def post_create(request):
    return render(request, 'main/post/post_create.html', {})


@login_required
def like_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    profile = request.user

    if profile in post.likes.all():
        post.likes.remove(profile)
    else:
        post.likes.add(profile)

    return redirect(request.META.get("HTTP_REFERER", "/"))

@login_required
def save_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    profile = request.user

    if profile in post.saves.all():
        post.saves.remove(profile)
    else:
        post.saves.add(profile)

    return redirect(request.META.get("HTTP_REFERER", "/"))
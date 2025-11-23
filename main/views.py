from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from .recs import get_recomended_posts


def home_page(request):
    posts = Post.objects.all()
    
    return render(request, 'main/base.html', {'posts': posts,})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    total_likes = post.total_likes_post()
    total_saves = post.total_saves_post()
    recommendations = get_recomended_posts(post)
    return render(request, 'main/post/post_detail.html', {'post': post, 'total_likes': total_likes, 'total_saves': total_saves, 'recommendations': recommendations})


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('main:home_page')
    return render(request, 'main/post/post_create.html', {'form': form,})


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
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .forms import CustomProfileCreationForm, CustomProfileAuthenticationForm, CustomProfileUptadeForm
from .models import Profile
from django.contrib import messages
from main.models import Post


def register(request):
  form = CustomProfileCreationForm(request.POST, request.FILES)
  if request.method == "POST":
      if form.is_valid():
        user = form.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('users:profile')  
  return render(request, 'users/register.html', {'form': form})
  

def login_view(request):
  form = CustomProfileAuthenticationForm(request, data=request.POST or None)


  if request.method == 'POST':
      if form.is_valid():
          user = form.get_user()
          login(request, user)
          return redirect('main:home_page')
      else:
          messages.error(request, 'Неверные данные')

  return render(request, 'users/login.html', {'form': form})
  

@login_required(login_url='/users/login')
def profile_view(request):
  if request.method == 'POST':
    form = CustomProfileUptadeForm(request.POST, instance=request.user)
    if form.is_valid():
      form.save()
      if request.headers.get('HX-Request'):
        return HttpResponse(headers={'HX-Redirect': reverse('users:profile')})
      return redirect(reverse('users:profile'))
  else:
    form = CustomProfileUptadeForm(instance=request.user)
    profile = Profile.objects.get(id=request.user.id)
    posts = Post.objects.filter(author=request.user.username).order_by('-published_at')
    posts_saved = request.user.saved_posts.all()


    return TemplateResponse(request, 'users/profile.html', {'form': form, 'profile': profile, 'posts': posts, 'posts_saved': posts_saved})
  
  recomended_posts = Post.objects.order_by('-created_at')[:5]

  return TemplateResponse(request, 'users/profile.html', {'form': form, 'profile': request.profile, 'recomended_posts': recomended_posts})

@login_required(login_url='/users/login')
def account_details(request):
  profile = Profile.objects.get(id=request.user.id)
  return TemplateResponse(request, 'users/partials/account_details.html', {'profile': profile})

@login_required(login_url='/users/login')
def edit_account_details(request):
    if request.method == "POST":
        form = CustomProfileUptadeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = CustomProfileUptadeForm(instance=request.user)

    return TemplateResponse(
        request,
        'users/partials/edit_account_details.html',
        {'profile': request.user, 'form': form}
    )


def update_account_details(request):
  if request.method == 'POST':
    form = CustomProfileUptadeForm(request.POST, instance=request.user)
    if form.is_valid():
      user = form.save(commit = False)
      user.clean()
      user.save()
      updeted_profile = Profile.objects.get(id=user.id)
      request.profile = updeted_profile
      if request.headers.get('HX-Request'):
        return TemplateResponse(request, 'users/partials/account_details.html', {'profile': updeted_profile})
      return TemplateResponse(request, 'users/partials/account_details.html', {'profile': updeted_profile})
    else:
      return TemplateResponse(request, 'users/partials/edit_account_details.html', 
                              {'profile': request.user,'form': form})
  if request.headers.get('HX-Request'):
    return HttpResponse(headers={'HX-Redirect': reverse('users:profile')})
  return redirect('users:profile')


def logout_view(request):
  logout(request)
  if request.headers.get('HX-Request'):
    return HttpResponse(headers={'HX-Redirect': reverse('main:home_page')})
  return redirect('main:home_page')
    

    

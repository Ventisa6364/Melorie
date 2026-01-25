from django.urls import path
from presentation.view import views_users
from data.models.models_users import Profile
from data.models.models_posts import Post

app_name = 'users'

urlpatterns = [
    path('register/', views_users.register, name='register'),
    path('login/', views_users.login_view, name='login'),
    path('profile/', views_users.profile_view, name='profile'),
    path('profile_author/', views_users.profile_author_view, name='profile_author'),
    path('account-details/', views_users.account_details, name='account_details'),
    path('account-edit/', views_users.edit_account_details, name='edit_account_details'),
    path('update-account-details/', views_users.update_account_details, name='update_account_details'),
    path('logout/', views_users.logout_view, name='logout'),
]
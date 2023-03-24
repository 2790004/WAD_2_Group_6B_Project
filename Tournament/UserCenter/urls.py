from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('sign_out/', views.sign_out, name='sign_out'),

    # user repath to avoid conflict with admin login
    re_path('.*', views.login, name='login'),
]

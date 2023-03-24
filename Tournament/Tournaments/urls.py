from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # Tournament index page
]

"""Tournament URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.views import static
from django.conf import settings
from .settings import DEBUG, static_token_str, media_token_str, admin_url_path, MEDIA_URL, MEDIA_ROOT

from UserCenter import urls as UserCenter_urls
from Teams import urls as Teams_urls
from Tournaments import urls as Tournaments_urls
import Home.views as Home_views

urlpatterns = []
if not DEBUG:
    urlpatterns = [
        # Use re_path() instead of path() to avoid the conflict error
        re_path(r'^' + static_token_str + '/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT},
                name='static'), ]

urlpatterns = urlpatterns + [
    re_path(r'^' + media_token_str + '/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT},
            name='media'),
    re_path('^' + admin_url_path + '/?', admin.site.urls),

    path('UserCenter/', include(UserCenter_urls)),
    path('Teams/', include(Teams_urls)),
    path('Tournaments/', include(Tournaments_urls)),
    re_path('.*', Home_views.home, name='Home'),

]

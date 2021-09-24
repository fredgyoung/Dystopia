"""config URL Configuration

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
from django.urls import path
from . import views

# Set the application namespace
#app_name = 'dystopia'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    # Authors
    path('authors-starting-with-<str:letter>/', views.author_list_view, name='author_list'),
    path('author/<slug:slug>/', views.author_detail_view, name='author_detail'),
    # Series
    path('series-starting-with-<str:letter>/', views.series_list_view, name='series_list'),
    path('series/<slug:slug>/', views.series_detail_view, name='series_detail'),
]


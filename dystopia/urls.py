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
    # Books
    path('books-starting-with-<str:letter>/', views.BookListView.as_view()),
    path('book/<slug:slug>/', views.BookDetailView.as_view(), name='book_detail'),

    #path('book/<slug:slug>/', views.book_detail_view, name='book_detail'),
    #path('books-starting-with-<str:letter>/', views.book_list_view, name='book_list'),
    # Main Admin Page
    #path('admin-reports/', views.admin_reports_view, name='admin_reports'),
    # Additional Admin Pages
    #path('admin-author-list/', views.admin_author_list_view, name='author_list'),
    #path('admin-book-list/', views.admin_book_list_view, name='book_list'),
    #path('admin-series-list/', views.admin_series_list_view, name='series_list'),
    #path('series-book-totals/', views.series_book_totals, name='series_list'),
    #path('books-without-amazon-link/', views.books_without_amazon_link, name='book_list'),

]


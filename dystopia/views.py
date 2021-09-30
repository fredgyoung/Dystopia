from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View, TemplateView
from django.views.generic import ListView, DetailView
from .models import Author, Book, Series
from django.db.models import Count


def home_page_view(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)

def author_list_view(request, letter):
    try:
        author_list = Author.objects.filter(last_names__startswith=letter)
    except:
        raise Http404(f"No authors beginning with {letter}!")
    return render(request, 'author_list.html', {'author_list': author_list})

def author_detail_view(request, slug):
    author = get_object_or_404(Author, slug=slug)
    book_list = author.books.all().order_by('reading_order')
    context = {
        'author': author,
        'book_list': book_list,
    }
    return render(request, 'author_detail.html', context)

def series_list_view(request, letter):
    try:
        series_list = Series.objects.filter(title__startswith=letter)
    except:
        raise Http404(f"No series beginning with {letter}!")
    return render(request, 'series_list.html', {'series_list': series_list})

def series_detail_view(request, slug):
    series = get_object_or_404(Series, slug=slug)
    book_list = series.books.all().order_by('reading_order')
    context = {
        'series': series,
        'book_list': book_list
    }
    return render(request, 'series_detail.html', context)

def book_list_view(request, letter):
    try:
        book_list = Book.objects.filter(title__startswith=letter)
    except:
        raise Http404(f"No books beginning with {letter}!")
    return render(request, 'book_list.html', {'book_list': book_list})

def book_detail_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context)


class SeriesDetailView(DetailView):
    model = Series
    template_name = 'series_detail.html'
    context_object_name = 'series'


# Admin Views
# List all authors
def admin_author_list_view(request):
    try:
        author_list = Author.objects.all()
    except:
        raise Http404(f"No authors!")
    return render(request, 'admin_author_list.html', {'author_list': author_list})

# List all books ordered by slug
def admin_book_list_view(request):
    try:
        book_list = Book.objects.all().order_by('slug')
    except:
        raise Http404(f"No books!")
    return render(request, 'admin_book_list.html', {'book_list': book_list})

# List all series order by title
def admin_series_list_view(request):
    try:
        series_list = Series.objects.all().order_by('title')
    except:
        raise Http404(f"No series!")
    return render(request, 'admin_series_list.html', {'series_list': series_list})

# List series and number of related books
def series_book_totals(request):
    try:
        #series_book_totals = Series.objects.annotate(num_books=Count('books')).order_by('title')
        series_book_totals = Series.objects.annotate(num_books=Count('books')).order_by('num_books', 'title')

    except:
        raise Http404(f"No series!")
    return render(request, 'series_book_totals.html', {'series_book_totals': series_book_totals})

'''
Proposed Views:
books without author
books without subtitle
books without series
books without slug 
books without description

series without author
series without slug
series without wikipedia, amazon, goodreads, author, or publisher webpage
series without description
series that are hidden
 
authors without wikipedia, author, or publisher webpage
'''
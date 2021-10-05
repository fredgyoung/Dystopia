from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View, TemplateView
from django.views.generic import ListView, DetailView
from .models import Author, Book, Series
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def home_page_view(request):
    template = 'home.html'
    context = {}
    return render(request, template, context)

def author_list_view(request, letter):
    author_list = Author.objects.filter(last_names__startswith=letter)
    context = {
        'letter': letter,
        'author_list': author_list,
    }
    return render(request, 'author_list.html', context)

def author_detail_view(request, slug):
    author = get_object_or_404(Author, slug=slug)
    book_list = author.books.all().order_by('reading_order')
    context = {
        'author': author,
        'book_list': book_list,
    }
    return render(request, 'author_detail.html', context)

def series_list_view(request, letter):
    series_list = Series.objects.filter(title__startswith=letter)
    context = {
        'letter': letter,
        'series_list': series_list,
    }
    return render(request, 'series_list.html', context)

def series_detail_view(request, slug):
    series = get_object_or_404(Series, slug=slug)
    book_list = series.books.all().order_by('reading_order')
    context = {
        'series': series,
        'book_list': book_list
    }
    return render(request, 'series_detail.html', context)

'''
# First Iteration
def book_list_view(request, letter):
    book_list = Book.objects.filter(title__startswith=letter)
    context = {
        'letter': letter,
        'book_list': book_list,
    }
    return render(request, 'book_list.html', context)

# Add Pagination
def book_list_view(request, letter):
    book_list = Book.objects.filter(title__startswith=letter)
    paginator = Paginator(book_list, 25) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'letter': letter,
        'page_obj': page_obj,
    }
    return render(request, 'book_list.html', context)
'''

class BookListView(ListView):
    paginate_by = 25
    context_obj_name = 'page_obj'
    template_name = 'book_list.html'

    def get_queryset(self):
        return Book.objects.filter(title__startswith=self.kwargs['letter'])

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the letter
        context['letter'] = self.kwargs['letter']
        return context


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
# Admin Homepage
@login_required
def admin_reports_view(request):
    return render(request, 'admin_reports.html')

# List all authors
@login_required
def admin_author_list_view(request):
    author_list = Author.objects.all()
    return render(request, 'admin_author_list.html', {'author_list': author_list})

# List all books ordered by slug
@login_required
def admin_book_list_view(request):
    book_list = Book.objects.all().order_by('slug')
    return render(request, 'admin_book_list.html', {'book_list': book_list})

# List all series order by title
@login_required
def admin_series_list_view(request):
    series_list = Series.objects.all().order_by('title')
    return render(request, 'admin_series_list.html', {'series_list': series_list})

# List series and number of related books
@login_required
def series_book_totals(request):
    series_book_totals = Series.objects.annotate(num_books=Count('books')).order_by('num_books', 'title')
    return render(request, 'series_book_totals.html', {'series_book_totals': series_book_totals})

# Books without an Amazon short link
@login_required
def books_without_amazon_link(request):
    book_list = Book.objects.filter(amazon_short_link__exact=None).order_by('series', 'title')
    return render(request, 'books_without_amazon_link.html', {'book_list': book_list})

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
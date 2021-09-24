from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic.base import View, TemplateView
from django.views.generic import ListView, DetailView
from .models import Author, Series


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


class SeriesDetailView(DetailView):
    model = Series
    template_name = 'series_detail.html'
    context_object_name = 'series'



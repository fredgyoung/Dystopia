from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from .models import Publisher, Imprint, Series, Author, Book


@admin.register(Imprint)
class ImprintAdmin(ModelAdmin):
    fields = (('title', 'slug'), 'website', 'publisher')
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class ImprintInline(TabularInline):
    model = Imprint
    #fields = ('publication_order', 'chronological_order', 'title', 'length')
    #ordering = ('publication_order',)
    prepopulated_fields = {'slug': ('title',)}
    extra = 10


@admin.register(Publisher)
class PublisherAdmin(ModelAdmin):
    inlines = [ImprintInline]

    fields = (
        ('title', 'slug'),
        'website',
    )

    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class BookInline(TabularInline):
    model = Book

    fields = (
        'publication_month',
        'publication_year',
        'reading_order',
        'title',
        'subtitle',
        'author',
        'length',
    )

    #prepopulated_fields = {'slug': ('title',)}
    ordering = ('reading_order', 'publication_year', 'publication_month',)
    extra = 10


@admin.register(Series)
class SeriesAdmin(ModelAdmin):
    inlines = [BookInline]

    fields = (
        ('title', 'slug'),
        'author',
        'wikipedia_page',
        'amazon_page',
        'goodreads_page',
        'author_website',
        'publisher_website',
        'notes',
    )

    list_display = ('title',)

    prepopulated_fields = {
        'slug': ('title',)
    }


class SeriesInline(TabularInline):
    model = Series
    fields = ('title',)
    ordering = ('title',)
    extra = 1


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    inlines = [SeriesInline]

    fields = (
        'first_names',
        'last_names',
        'slug',
        'wikipedia_page',
        'author_website',
        'publisher_website',
    )

    prepopulated_fields = {
        'slug': ('first_names', 'last_names')
    }


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('title', 'subtitle', 'series', 'author')
    list_filter = ('series',)

    fields = (
        ('title', 'subtitle'),
         'slug',
        ('author', 'length'),
        'series',
        ('publication_month', 'publication_year'),
        'asin',
        'amazon_short_link',
    )

    prepopulated_fields = {
        'slug': ('title', 'subtitle')
    }



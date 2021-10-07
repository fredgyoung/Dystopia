from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from .models import Series, Author, Book


class BookInline(StackedInline):
    model = Book
    readonly_fields = ('slug',)
    raw_id_fields = ('author',)

    fields = (
        ('reading_order', 'author'),
        ('title', 'subtitle'),
        ('amazon_short_link', 'length'),
    )

    ordering = ('reading_order', 'publication_year', 'publication_month',)
    extra = 0


@admin.register(Series)
class SeriesAdmin(ModelAdmin):
    inlines = [BookInline]
    readonly_fields = ('slug',)
    raw_id_fields = ('author',)

    fields = (
        'publish',
        ('title', 'slug'),
        'author',
        'wikipedia_page',
        'amazon_page',
        'goodreads_page',
        'author_website',
        'publisher_website',
        'notes',
    )

    list_display = ('title', 'author', 'publish')
    list_filter = ('publish',)
    search_fields = ('title', 'author__first_names', 'author__last_names',)


class SeriesInline(StackedInline):
    model = Series
    readonly_fields = ('slug',)

    fields = (
        'publish',
        ('title', 'slug'),
        'wikipedia_page',
        'amazon_page',
        'goodreads_page',
        'author_website',
        'publisher_website',
        'notes',
    )

    ordering = ('title',)

    extra = 0


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    inlines = [SeriesInline, BookInline]
    readonly_fields = ('id', 'slug',)
    search_fields = ['last_names', 'first_names']
    list_display = ['last_name_first_name', 'publish']
    list_filter = ['publish',]

    fields = (
        'publish',
        ('first_names', 'id'),
        ('last_names', 'slug'),
        'wikipedia_page',
        'author_website',
        'publisher_website',
    )


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('title', 'publish', 'series', 'author')
    list_filter = ['publish',]
    readonly_fields = ('slug',)
    search_fields = ('title', 'author__first_names', 'author__last_names',)
    raw_id_fields = ('author', 'series')

    fields = (
        'publish',
        ('title', 'slug'),
        'subtitle',
        'author',
        'series',
        'length',
        'amazon_short_link',
    )

from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from .models import Series, Author, Book


# Book
@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = ('title', 'publish', 'series', 'author')
    list_filter = ['publish',]
    readonly_fields = ('slug', 'id')
    search_fields = ('title', 'author__first_names', 'author__last_names',)
    raw_id_fields = ('author', 'series')
    list_editable = ['publish',]

    fields = (
        'publish',
        ('title', 'id'),
        ('author', 'slug'),
        'series',
        'length',
        'amazon_short_link',
        'amazon_small_image_anchor',
        'amazon_large_image_anchor',
        'notes',
        'description',
    )


# Series
class BookInlineForSeries(StackedInline):
    model = Book
    readonly_fields = ('series', )
    raw_id_fields = ('author', )

    fields = (
        #'publish',
        ('reading_order', 'series'),
        ('title', 'length'),
        #'amazon_short_link',
        'author',
        #'amazon_small_image_anchor',
        #'amazon_large_image_anchor',
    )

    ordering = ('reading_order', 'publication_year', 'publication_month',)
    extra = 0


@admin.register(Series)
class SeriesAdmin(ModelAdmin):
    inlines = [BookInlineForSeries]
    readonly_fields = ('slug', 'id', 'number_of_books')
    raw_id_fields = ('author',)
    list_editable = ['publish',]

    fields = (
        'publish',
        #('title', 'slug'),
        #('author', 'number_of_books'),
        'title',
        'slug',
        'number_of_books',
        'author',
        'wikipedia_page',
        'amazon_page',
        'goodreads_page',
        'author_website',
        'publisher_website',
        'notes',
        'description',
    )

    list_display = ('title', 'author', 'publish', 'number_of_books')
    list_filter = ('publish',)
    search_fields = ('title', 'author__first_names', 'author__last_names',)


# Author
class SeriesInlineForAuthor(StackedInline):
    model = Series
    readonly_fields = ('author', 'slug')

    fields = (
        ('publish', 'author'),
        ('title', 'slug'),
        'wikipedia_page',
        'amazon_page',
        'goodreads_page',
        'author_website',
        'publisher_website',
        'notes',
        'description',
    )

    ordering = ('title',)

    extra = 0


class BookInlineForAuthor(StackedInline):
    model = Book
    readonly_fields = ('author',)
    raw_id_fields = ('series',)

    fields = (
        #'publish',
        ('reading_order', 'author'),
        ('title', 'series'),
        #'amazon_short_link',
        'length',
        #'amazon_small_image_anchor',
        #'amazon_large_image_anchor',
    )

    ordering = ('reading_order', 'publication_year', 'publication_month',)
    extra = 0


@admin.register(Author)
class AuthorAdmin(ModelAdmin):
    inlines = [SeriesInlineForAuthor, BookInlineForAuthor]
    readonly_fields = ('id', 'slug', 'number_of_series', 'number_of_books')
    search_fields = ['last_names', 'first_names']
    list_display = ['first_names', 'last_names', 'publish', 'number_of_series', 'number_of_books']
    list_filter = ['publish',]
    list_editable = ['publish',]
    list_display_links = ('first_names', 'last_names')

    fields = (
        'publish',
        'id',
        'slug',
        'first_names',
        'last_names',
        'number_of_series',
        'number_of_books',
        'wikipedia_page',
        'author_website',
        'publisher_website',
        'notes',
        'description',
    )



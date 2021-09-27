from django.contrib import admin
from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from .models import Publisher, Imprint, Series, Author, Book


@admin.register(Imprint)
class ImprintAdmin(ModelAdmin):
    fields = (('title', 'slug'), 'website', 'publisher')
    list_display = ('title',)


class ImprintInline(TabularInline):
    model = Imprint
    extra = 10


@admin.register(Publisher)
class PublisherAdmin(ModelAdmin):
    inlines = [ImprintInline]

    fields = (
        ('title', 'slug'),
        'website',
    )

    list_display = ('title',)


class BookInline(StackedInline):
    model = Book
    readonly_fields = ('slug',)

    fields = (
        'reading_order',
        #'publication_month',
        #'publication_year',
        ('title', 'slug'),
        'subtitle',
        'author',
        'length',
        'amazon_short_link',
    )

    ordering = ('reading_order', 'publication_year', 'publication_month',)
    extra = 0


@admin.register(Series)
class SeriesAdmin(ModelAdmin):
    inlines = [BookInline]
    #save_on_top = True
    readonly_fields = ('slug',)

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

    list_display = ('title', 'author')


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
    #save_on_top = True
    inlines = [SeriesInline, BookInline]
    readonly_fields = ('slug',)

    fields = (
        ('first_names', 'slug'),
        'last_names',
        'wikipedia_page',
        'author_website',
        'publisher_website',
    )


@admin.register(Book)
class BookAdmin(ModelAdmin):
    #save_on_top = True
    list_display = ('title', 'subtitle', 'series', 'author')
    list_filter = ('series',)
    readonly_fields = ('slug',)

    fields = (
        ('title', 'slug'),
        'subtitle',
        'author',
        'length',
        'series',
        #'publication_month',
        #'publication_year',
        'amazon_short_link',
    )

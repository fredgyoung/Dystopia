from django.db import models
from django.utils.dates import MONTHS
from django.utils.text import slugify


class Author(models.Model):

    publish = models.BooleanField(default=False)

    first_names = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=""
    )

    last_names = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default=""
    )

    slug = models.SlugField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
    )

    wikipedia_page = models.URLField(
        verbose_name="Wikipedia Page",
        null=True,
        blank=True,
    )

    amazon_page = models.URLField(
        verbose_name="Amazon Page",
        null=True,
        blank=True,
    )

    goodreads_page = models.URLField(
        verbose_name="Goodreads' Page",
        null=True,
        blank=True,
    )

    author_website = models.URLField(
        verbose_name="Author's Website",
        null=True,
        blank=True,
    )

    publisher_website = models.URLField(
        verbose_name="Publisher's Website",
        null=True,
        blank=True,
    )

    notes = models.TextField(
        verbose_name="Internal Notes",
        null=True,
        blank=True
    )

    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.id}-{self.first_names}-{self.last_names}")
        super(Author, self).save(*args, **kwargs)

    @property
    def first_name_last_name(self):
        return f'{self.first_names} {self.last_names}'

    @property
    def last_name_first_name(self):
        return f'{self.last_names}, {self.first_names}'

    @property
    def number_of_series(self):
        return Series.objects.filter(author__exact=self.id).count()

    @property
    def number_of_books(self):
        return Book.objects.filter(author__exact=self.id).count()

    def __str__(self):
        return self.first_name_last_name

    class Meta:
        verbose_name_plural = 'Authors'
        ordering = ['first_names', 'last_names']


class Series(models.Model):

    publish = models.BooleanField(default=False)

    title = models.CharField(
        max_length=255,
    )

    wikipedia_page = models.URLField(
        verbose_name="Wikipedia Page",
        null=True,
        blank=True,
    )

    amazon_page = models.URLField(
        verbose_name="Amazon Page",
        null=True,
        blank=True,
    )

    goodreads_page = models.URLField(
        verbose_name="Goodreads' Page",
        null=True,
        blank=True,
    )

    author_website = models.URLField(
        verbose_name="Author's Website",
        null=True,
        blank=True,
    )

    publisher_website = models.URLField(
        verbose_name="Publisher's Website",
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        max_length=255,
        null=True,
        blank=True,
        #unique=True
    )

    author = models.ForeignKey(
        Author,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='series',
    )

    notes = models.TextField(
        verbose_name="Internal Notes",
        null=True,
        blank=True
    )

    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.id}-the-{self.title}-series")
        super(Series, self).save(*args, **kwargs)

    @property
    def number_of_books(self):
        return Book.objects.filter(series__exact=self.id).count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Series'
        ordering = ['title']


class Book(models.Model):

    LENGTH_CHOICES = [
        ('Comic', 'Comic'),
        ('Graphic Novel', 'Graphic Novel'),
        ('Manga', 'Manga'),
        ('Novel', 'Novel'),
        ('Novella', 'Novella'),
        ('Short Story', 'Short Story'),
        ('Short Story Collection', 'Short Story Collection'),
    ]

    publish = models.BooleanField(default=False)

    title = models.CharField(
        max_length=255,
    )

    slug = models.SlugField(
        max_length=255,
        null=True,
        blank=True,
        unique=True
    )

    length = models.CharField(
        max_length=255,
        choices=LENGTH_CHOICES,
        default='Novel',
        null=True,
        blank=True,
    )

    # Author 211 is "No Author"
    DEFAULT_AUTHOR_ID = 211

    author = models.ForeignKey(
        Author,
        #default=DEFAULT_AUTHOR_ID,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='books',
    )

    series = models.ForeignKey(
        Series,
        null=True,
        blank=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name='books',
    )

    publication_month = models.PositiveSmallIntegerField(
        choices=MONTHS.items(),
        null=True,
        blank=True,
    )

    publication_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    reading_order = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True
    )

    amazon_short_link = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Amazon Short Link",
    )

    amazon_small_image_anchor = models.TextField(
        null=True,
        blank=True,
        verbose_name="Amazon Small Image Anchor",
    )

    amazon_large_image_anchor = models.TextField(
        null=True,
        blank=True,
        verbose_name="Amazon Large Image Anchor",
    )

    notes = models.TextField(
        verbose_name="Internal Notes",
        null=True,
        blank=True
    )

    description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.id}-{self.title}-by-{self.author.first_name_last_name}")
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ['title']


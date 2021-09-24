from django.db import models
from django.utils.dates import MONTHS


class Publisher(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Publishers'
        ordering = ['title']


class Imprint(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    publisher = models.ForeignKey(
        Publisher,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Imprints'
        ordering = ['title']


class Author(models.Model):

    first_names = models.CharField(max_length=255)
    last_names = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)

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

    wikipedia_page = models.URLField(
        verbose_name="Wikipedia Page",
        null=True,
        blank=True,
    )

    #description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_names} {self.last_names}'

    def last_name_first_name(self):
        return f'{self.last_names}, {self.first_names}'

    class Meta:
        verbose_name_plural = 'Authors'
        ordering = ['last_names', 'first_names']


class Series(models.Model):

    title = models.CharField(
        max_length=255,
        unique=True
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
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        Author,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='series',
    )

    notes = models.TextField(
        verbose_name="Internal Notes",
        null=True,
        blank=True,
    )

    #description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Series'
        ordering = ['title']


class Book(models.Model):

    LENGTH_CHOICES = [
        ('Novel', 'Novel'),
        ('Novella', 'Novella'),
        ('Short Story', 'Short Story'),
        ('Short Story Collection', 'Short Story Collection'),
    ]

    title = models.CharField(
        max_length=255,
    )

    subtitle = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        null=True,
        blank=True
    )

    length = models.CharField(
        max_length=255,
        choices=LENGTH_CHOICES,
        default='Novel',
        null=True,
        blank=True,
    )

    author = models.ForeignKey(
        Author,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='books',
    )

    #description = models.TextField(null=True, blank=True)

    series = models.ForeignKey(
        Series,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
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
        null=True,
        blank=True,
        verbose_name="Amazon Short Link",
    )

    def __str__(self):
        return self.title
        '''
        if self.title[:4] == "The ":
            return f"{self.title[4:]}, {self.title[:4]}"
        else:
            return self.title
        '''

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ['title']

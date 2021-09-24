# Generated by Django 3.2.6 on 2021-09-11 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0041_series_amazon_page'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='wikipedia',
            new_name='wikipedia_page',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='wikipedia',
            new_name='wikipedia_page',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publication_order',
        ),
        migrations.AddField(
            model_name='series',
            name='author_website',
            field=models.URLField(blank=True, null=True, verbose_name="Author's Website"),
        ),
    ]
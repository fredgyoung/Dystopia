# Generated by Django 3.2.6 on 2021-09-26 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0050_alter_book_amazon_short_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
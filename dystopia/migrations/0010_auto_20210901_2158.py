# Generated by Django 3.2.6 on 2021-09-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0009_auto_20210825_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='series',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
# Generated by Django 3.2.6 on 2021-09-26 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0054_alter_series_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

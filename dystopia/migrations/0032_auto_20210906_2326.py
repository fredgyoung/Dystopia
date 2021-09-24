# Generated by Django 3.2.6 on 2021-09-07 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0031_auto_20210906_2323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='website',
            new_name='publisher_website',
        ),
        migrations.RenameField(
            model_name='series',
            old_name='website',
            new_name='publisher_website',
        ),
        migrations.AddField(
            model_name='author',
            name='author_website',
            field=models.URLField(blank=True, null=True, verbose_name="Author's Website"),
        ),
    ]

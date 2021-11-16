# Generated by Django 3.2.8 on 2021-11-16 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0086_alter_book_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='length',
            field=models.CharField(blank=True, choices=[('Comic', 'Comic'), ('Graphic Novel', 'Graphic Novel'), ('Manga', 'Manga'), ('Novel', 'Novel'), ('Novella', 'Novella'), ('Short Story', 'Short Story'), ('Short Story Collection', 'Short Story Collection')], default='Novel', max_length=255, null=True),
        ),
    ]

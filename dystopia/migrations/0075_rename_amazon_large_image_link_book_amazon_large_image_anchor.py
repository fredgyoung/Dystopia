# Generated by Django 3.2.6 on 2021-10-16 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0074_auto_20211016_1456'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='amazon_large_image_anchor',
            new_name='amazon_large_image_anchor',
        ),
    ]
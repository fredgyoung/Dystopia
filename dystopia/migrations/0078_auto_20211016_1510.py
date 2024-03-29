# Generated by Django 3.2.6 on 2021-10-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0077_auto_20211016_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='amazon_large_image_anchor',
            field=models.TextField(blank=True, max_length=1024, null=True, verbose_name='Amazon Large Image Anchor'),
        ),
        migrations.AddField(
            model_name='book',
            name='amazon_small_image_anchor',
            field=models.TextField(blank=True, max_length=1024, null=True, verbose_name='Amazon Small Image Anchor'),
        ),
    ]

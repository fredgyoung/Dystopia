# Generated by Django 3.2.8 on 2021-11-09 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0081_auto_20211021_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Internal Notes'),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Internal Notes'),
        ),
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
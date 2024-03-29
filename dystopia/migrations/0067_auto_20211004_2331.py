# Generated by Django 3.2.6 on 2021-10-05 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0066_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='amazon_short_link',
            field=models.URLField(blank=True, default='https://amzn.to/3l2b6VO', max_length=30, null=True, verbose_name='Amazon Short Link'),
        ),
    ]

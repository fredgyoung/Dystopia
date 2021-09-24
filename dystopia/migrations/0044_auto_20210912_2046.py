# Generated by Django 3.2.6 on 2021-09-13 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0043_rename_chronological_order_book_reading_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='subtitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]

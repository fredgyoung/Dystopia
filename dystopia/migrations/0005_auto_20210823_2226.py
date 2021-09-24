# Generated by Django 3.2.6 on 2021-08-24 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0004_author_suffix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

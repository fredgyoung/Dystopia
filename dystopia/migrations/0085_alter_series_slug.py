# Generated by Django 3.2.8 on 2021-11-10 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0084_auto_20211109_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]

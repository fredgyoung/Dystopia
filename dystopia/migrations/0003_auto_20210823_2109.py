# Generated by Django 3.2.6 on 2021-08-24 01:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0002_auto_20210823_2105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title'], 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name'], 'verbose_name_plural': 'Publishers'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['title'], 'verbose_name_plural': 'Series'},
        ),
        migrations.RenameField(
            model_name='author',
            old_name='first_names',
            new_name='first_name',
        ),
    ]

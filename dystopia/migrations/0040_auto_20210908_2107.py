# Generated by Django 3.2.6 on 2021-09-09 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0039_remove_author_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='chronological_sequence',
            new_name='chronological_order',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publication_sequence',
            new_name='publication_order',
        ),
    ]

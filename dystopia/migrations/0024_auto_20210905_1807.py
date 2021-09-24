# Generated by Django 3.2.6 on 2021-09-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0023_imprint_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='imprint',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]

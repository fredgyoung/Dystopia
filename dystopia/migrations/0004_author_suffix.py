# Generated by Django 3.2.6 on 2021-08-24 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0003_auto_20210823_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='suffix',
            field=models.CharField(blank=True, choices=[('Sr.', 'Sr.'), ('Jr.', 'Jr.'), ('II', 'II'), ('III', 'III')], max_length=10, null=True),
        ),
    ]

# Generated by Django 3.2.6 on 2021-09-08 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dystopia', '0032_auto_20210906_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='notes',
            field=models.TextField(blank=True, null=True, verbose_name='Internal Notes'),
        ),
    ]

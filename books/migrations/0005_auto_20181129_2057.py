# Generated by Django 2.1.3 on 2018-11-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20181129_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='url',
            field=models.URLField(unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
# Generated by Django 4.0.1 on 2022-01-12 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_rename_posts_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='create_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='update_date',
        ),
    ]

# Generated by Django 3.1.4 on 2020-12-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read_books', '0007_book_picture_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
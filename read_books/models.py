from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django import forms

#from .management.commands import config


class Category(models.Model):
    """category models"""
    category_name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name


class BookManager(models.Manager):
    """manager find product substitutes"""

    def search_book(self, book_name):
        """check if substitutes exists in database"""

        book = Book.objects.filter(
            Q(book_name__icontains=book_name) |
            Q(author__icontains=book_name
              ))[:1].get()

        return book

    def get_detail(self, book_id):
        """get detail of product"""

        try:
            book = Book.objects.get(id=book_id)

        except Book.DoesNotExist:
            book = None

        finally:
            return book

    def add_substitute(self, book_original_id, book_substitute_id, user):
        """save substitute in favoris"""

        Substitute.objects.update_or_create(
            book_substitute_id=book_substitute_id,
            book_original_id=book_original_id,
            customuser=user
        )


class Book(models.Model):
    """product model"""
    id = models.BigIntegerField(primary_key=True)
    book_name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    objects = BookManager()

    class Meta:
        ordering = ['book_name']

    def __str__(self):
        return self.book_name


class Substitute(models.Model):
    """substitute model"""

    book_original = models.ForeignKey(Book,
                                         on_delete=models.CASCADE, related_name='book_original')
    book_substitute = models.ForeignKey(Book,
                                           on_delete=models.CASCADE, related_name='book_substitute')
    objects = BookManager()

    def __str__(self):

        return str(self.book_substitute)
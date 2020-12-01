from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django import forms

class Category(models.Model):
    """category models"""
    category_name = models.CharField(max_length=150, unique=True,null=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

class BookManager(models.Manager):
    """manager book function"""

    def add_book(self, book_id,title):
        """save book in favoris"""

        Book.objects.update_or_create(
            id=book_id,
            book_name=title
        )

class Book(models.Model):
    """book model"""
    id = models.BigIntegerField(primary_key=True)
    book_name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    comment = models.CharField(max_length=150)
    picture = models.CharField(max_length=350)
    objects = BookManager()

    class Meta:
        ordering = ['book_name']

    def __str__(self):
        return self.book_name




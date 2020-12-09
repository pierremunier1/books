from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django import forms
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator



class Category(models.Model):
    """category models"""
    category_name = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

class BookManager(models.Manager):
    """manager book function"""

    def add_book(self, book_id,title,book_cat,picture,picture_detail,user,description,author):
        """save book in favoris"""

        c1, created = Category.objects.get_or_create(
                            category_name=book_cat
                            )

        c2, created = CustomUser.objects.get_or_create(
                        username=user
                        )

        Book.objects.update_or_create(
            id=book_id,
            book_name=title,
            category=c1,
            picture=picture,
            picture_detail=picture_detail,
            customuser=c2,
            description=description,
            author=author
           
        )

class Book(models.Model):
    """book model"""
    id = models.BigIntegerField(primary_key=True)
    book_name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.CharField(max_length=10000)
    picture = models.CharField(max_length=350)
    picture_detail = models.CharField(max_length=350)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    customuser = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    
    score = models.IntegerField(default=0,
    validators=[
        MaxValueValidator(5),
        MinValueValidator(0),
    ]
    )

    objects = BookManager()

    class Meta:
        ordering = ['book_name']
        verbose_name = 'book'
      

    def __str__(self):
        return self.book_name


    

  

   
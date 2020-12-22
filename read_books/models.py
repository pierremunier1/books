from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django import forms
from django.utils import timezone
from users.models import CustomUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Category(models.Model):
    """category models"""
    category_name = models.CharField(max_length=150, unique=True,null=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

class BookManager(models.Manager):
    """manager book function"""

    def add_book(self,book_id,user,title,book_cat,picture,picture_detail,description,author):
        """save book in favoris"""

        self.book_id = book_id

        c1, created = Category.objects.get_or_create(
                            category_name=book_cat
                            )
        
        Book.objects.get_or_create(
            id=self.book_id,
            book_name=title,
            category=c1,
            picture=picture,
            picture_detail=picture_detail,
            description=description,
            author=author
           
        )
        
        Favorite.objects.get_or_create(
            book_fav_id=self.book_id,
            customuser=user
        )

class Book(models.Model):
    """book model"""
    id = models.CharField(max_length=20,primary_key=True)
    book_name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.CharField(max_length=10000)
    picture = models.CharField(max_length=350)
    picture_detail = models.CharField(max_length=350)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )
    likes=models.ManyToManyField(CustomUser,related_name='likes',blank=True)
    
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

    def likecount(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('favorite',kwargs={'book_id': self.id})

class Favorite(models.Model):
    """substitute model"""

    customuser = models.ForeignKey(
        'users.CustomUser', on_delete=models.CASCADE)
    book_fav = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='book_fav')
                                         
    objects = BookManager()

    def __str__(self):

        return str(self.book_fav)
    

class Comment(models.Model):

    book = models.ForeignKey(Book, on_delete = models.CASCADE) 
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE) 
    content = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'comment on {} by {}'.format(self.book.book_name,self.user.username)
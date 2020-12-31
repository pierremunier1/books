from django.db import models
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django import forms
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse
from taggit.managers import TaggableManager
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

UserModel = get_user_model()

class Category(models.Model):
    """contains all fields of category model"""
    category_name = models.CharField(max_length=150, unique=True,null=True)

    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name

class BookManager(models.Manager):
    """manager book function"""

    def add_book(self,book_id,user,title,book_cat,picture,picture_detail,description,author):
        """save book in favorite"""

        self.book_id = book_id

        # create category for book
        c1, created = Category.objects.get_or_create(
                            category_name=book_cat
                            )
        # add book into the table
        Book.objects.get_or_create(
            google_id=self.book_id,
            book_name=title,
            slug=slugify(title),
            category=c1,
            picture=picture,
            picture_detail=picture_detail,
            description=description,
            author=author
           
        )
        
        #create an id for favorite and django-taggit
        book=Book.objects.filter(google_id=self.book_id).first()
        
        #add book into the favorite
        Favorite.objects.get_or_create(
            book_favorites_id=book.id,
            customuser=user
        )

class Book(models.Model):
    """contain all fields of book model"""
    
    google_id = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    book_name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    description = models.CharField(max_length=10000)
    picture = models.CharField(max_length=350)
    picture_detail = models.CharField(max_length=350)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,null=True
    )
    objects = BookManager()
    tags = TaggableManager()
    ratings = GenericRelation(Rating, related_query_name='books')

    class Meta:
        ordering = ['book_name']
        verbose_name = 'book'

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('favorite',kwargs={'slug': self.slug})

class Favorite(models.Model):
    """contains all field of favorite model"""

    customuser = models.ForeignKey(
        UserModel, on_delete=models.CASCADE)
    book_favorites = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='book_favorites')
                                         
    objects = BookManager()

    def __str__(self):

        return str(self.book_favorites)
    

class Comment(models.Model):
    """contains all fields of comment model"""

    book = models.ForeignKey(Book, on_delete = models.CASCADE) 
    user = models.ForeignKey(UserModel, on_delete = models.CASCADE) 
    content = models.TextField() 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'comment on {} by {}'.format(self.book.book_name,self.user.username)
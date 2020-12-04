
from django.contrib import admin
from .models import Category, Book
from star_ratings.models import Rating

admin.site.register(Category)
admin.site.register(Book)





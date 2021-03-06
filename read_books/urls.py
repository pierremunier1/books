"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views
from django.views.generic.base import TemplateView

appname='read_books'

urlpatterns = [
    
    path('home', TemplateView.as_view(template_name='home.html'), name='home'),
    path('ajax', views.result, name='result'),
    path('<book_id>', views.detail, name='book'),
    path('book/<str:book_id>', views.save_book, name='save_book'),
    path('favorite/', views.favorite, name='favorite'),
    path('favorite/<slug:slug>/', views.favorite_detail, name='favorite'),
    path('',views.best_book,name='home'),
    path('remove_book/<slug:slug>/',views.remove_book,name='remove_book'),
    path('tag/<slug:slug>/', views.tagged, name="tagged"),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    
    
   
   
]

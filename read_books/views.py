from django.shortcuts import render
from read_books.response import GoogleApi, Response
from django.http import JsonResponse
from read_books.models import Book

# Create your views here.

def search(request):
    """showing the home page"""

    return render(request, "home.html")

def result(request):
    """autocomplete research in database"""
    
    query = request.GET.get('query')
    
    user_text = Response.response_front(query)

    book = {
        'book': user_text
    }

    return render(request,
        "home.html",
        {
            "book": book
        }
    )


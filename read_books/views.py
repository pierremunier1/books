from django.shortcuts import render
from read_books.response import GoogleApi, Response
from django.http import JsonResponse
from read_books.models import Book

# Create your views here.

def search(request):
    """showing the home page"""

    return render(request, "home.html")

def search_autocomplete(request):
    """autocomplete research in database"""
    books = list()

    if 'term' in request.GET:
        qs = (
            Response.response_front(
                request.GET.get('term'))
                )
        for book in qs:
            books.append(qs)

    return JsonResponse(books[0]['title'],safe=False)

def result(request):

    if request.is_ajax:
        
        query = request.POST.get('query')

        book = Response.response_front(query)

        result = {'response':(book['response'][0])}

        return JsonResponse(result,safe=False)



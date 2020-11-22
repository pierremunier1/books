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

    books = list()
    book_error = {'title':'incorrect'}

    if request.is_ajax:

        try:

            query = request.POST.get('query')
            
            assert len(query)>=2
            print(query)
            qs = Response.response_front(query)
        
            for book in qs:
                books.append(qs)

            result = {
                    'picture':(str(books[0]['picture'])[1:-1]),
                    'title':books[0]['title']
            }

            return JsonResponse(result,safe=False)

        except AssertionError:
            print('nombre de caracteres incorrect')
            return JsonResponse(book_error,safe=False)



from django.shortcuts import render
from read_books.response import GoogleApi, Response
from django.http import JsonResponse, HttpResponse
from read_books.models import Book



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
    """display result of get_books function"""

    books = list()
    book_error = 'incorrect'
    
    if request.is_ajax and request.method == "POST":

        try:
            query = request.POST.get('query')
        
            qs = Response.response_front(query)
    
            for book in qs:
                books.append(qs)

            result = {
                    'picture':(str(books[0]['picture'])[1:-1]),
                    'title':books[0]['title']
            }

            return JsonResponse(result,safe=False)


        except AssertionError:
            return HttpResponse(book_error)


def detail(request,book_id):

    try:
        if book_id is not None:
            book = Response.response_front(book_id)
            
        return render(
        request,
        "home.html",
        {
            "title":(str(book['title'][0])).replace("'"," "),
            "desc": (str(book['description'][0])).replace("'"," "),
            
        }
    )

    except AssertionError:
        return HttpResponse(book_error)







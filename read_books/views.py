from django.shortcuts import render,redirect
from read_books.response import GoogleApi, Response
from django.http import JsonResponse, HttpResponse
from read_books.models import Book



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
                    'picture':Response.build(books[0]['picture']),
                    'title':books[0]['title']
            }

            return JsonResponse(result,safe=False)

        except:
            return HttpResponse(book_error)


def detail(request,book_id):

    try:
        if book_id is not None:
            book = Response.response_front(book_id)

        return render(
        request,
        "book.html",
        {
            "title":Response.build(book['title'][0]),
            "desc": Response.build(book['description'][0]),
            "picture":book['picture'][0],
            "book_id":book_id,
            "book_cat":book['categorie'][0]
        }
    )
    except:
        return HttpResponse(book_error)

def save_book(request,book_id):
    """add book for later"""

    try:
        if book_id is not None:
            book = Response.response_front(book_id)

            Book.objects.add_book(
                book_id,
                title=book['title'][0],
                book_cat=Response.build(book['categorie'][0]),
                picture=book['picture'][0]
                )

        return redirect("home")

    except:
        return HttpResponse(book_error)
 


from django.shortcuts import render,redirect
from read_books.response import GoogleApi, Response
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from read_books.models import Book
from users.models import CustomUser
from django.contrib.auth.decorators import login_required


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

    book_error=('ko')

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

@login_required(login_url='/users/login/', redirect_field_name='next')
def save_book(request,book_id):
    """add book for later"""
    
    try:

        if book_id is not None:
            book = Response.response_front(book_id)

        if request.user.is_authenticated:
            user = get_object_or_404(
            CustomUser,
            id=request.user.id
        )
            Book.objects.add_book(
                book_id,
                title=(book['title'][0]),
                book_cat=Response.build(book['categorie'][0]),
                picture=book['picture'][0],
                user=user
                )

        return redirect("home")
    except:
        return HttpResponse('error')


#@login_required(login_url='/users/login/', redirect_field_name='next')
def favorite(request):
    """show favorite products"""

    books = Book.objects.filter(
        customuser=request.user)
    
    print(books)

    return redirect("favorite")
  

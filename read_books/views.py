from django.shortcuts import render,redirect
from read_books.response import GoogleApi, Response
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from read_books.models import Book
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from random import choice


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
            "book_cat":book['categorie'][0],
            "book_author":(book['author'][0])
            
        }
    )
    except:
        return HttpResponse(book_error)

#login_required(login_url='/users/login/', redirect_field_name='next')
def save_book(request,book_id):
    """add book for later"""
    
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
            description=book['description'][0],
            user=user,
            author=book['author'][0]
            )

    return redirect("home")
   
@login_required(login_url='/users/login/', redirect_field_name='next')
def favorite(request):
    """show favorite products"""

    books = Book.objects.filter(customuser=request.user).order_by('score')

    context={

        'books': books
    }

    return render(request, "favorite.html",context)

def favorite_detail(request,book_id):
    obj = Book.objects.filter(id=book_id).first()
    
    context ={
        'object': obj
    }
    return render(request, 'detail.html', context)


def rate_book(request):

    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        obj = Book.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})


def best_book(request):
    """show favorite products"""

    category_name = ('Music')

    b1 = Book.objects.filter(
        category__category_name='Music').order_by('score')[:5]
        
    b2 = Book.objects.filter(
        score__gte=0)[:5]

    b3 = Book.objects.filter(customuser=request.user).order_by('score')[:5]

    context={

        'best_books_1': b1,
        'best_books_2': b2,
        'best_books_3': b3
    }

    return render(request, "home.html",context)


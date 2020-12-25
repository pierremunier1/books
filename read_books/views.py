from django.shortcuts import render,redirect
from read_books.response import GoogleApi, Response
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from read_books.models import Book,Favorite,Comment
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import CommentForm,PostForm
from django.views.generic.detail import DetailView

def result(request):
    """display result of get_books function"""

    books = list()

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
        print('error')
    

def detail(request,book_id):
    """detail of book"""

    if book_id is not None:
        book = Response.response_front(book_id)
    
    comments=Comment.objects.filter(book=book_id).order_by('-pk')
        
    context = {
        "title":Response.build(book['title'][0]),
        "desc": Response.build(book['description'][0]),
        "picture_detail":book['picture_detail'][0],
        "book_id":book_id,
        "book_cat":book['categorie'][0],
        "book_author":(book['author'][0]),
        "comments":comments
        
    }
    return render(
    request,
    "book.html",context)

@login_required(login_url='/users/login/', redirect_field_name='next')
def save_book(request,book_id):
    """add book for later"""
    
    if request.user.is_authenticated:
        user = get_object_or_404(
        CustomUser,
        id=request.user.id
        )
        book = Response.response_front(book_id)
        
        Book.objects.add_book(
        book_id,
        user,
        title=(book['title'][0]),
        book_cat=Response.build(book['categorie'][0]),
        picture=book['picture'][0],
        picture_detail=book['picture_detail'][0],
        description=book['description'][0],
        author=book['author'][0]
        )

        Favorite.objects.add_book(
        book_id,
        user,
        title=(book['title'][0]),
        book_cat=Response.build(book['categorie'][0]),
        picture=book['picture'][0],
        picture_detail=book['picture_detail'][0],
        description=book['description'][0],
        author=book['author'][0]
        )
        

    return redirect("home")
   
@login_required(login_url='/users/login/?next=/favorite/', redirect_field_name='next')
def favorite(request):
    """show favorite books"""

    books = Book.objects.filter(customuser=request.user)

    context={

        'books': books
    }
    return render(request, "favorite.html",context)

def favorite_detail(request,book_id):
    """show book detail in favorite"""

    obj = Book.objects.filter(id=book_id).first()
    comments=Comment.objects.filter(book=obj).order_by('-pk')

    if request.method == 'POST': 
        cf = CommentForm(request.POST or None) 
        if cf.is_valid(): 
            content = request.POST.get('content') 
            comment = Comment.objects.create(
                book = obj, user = request.user, content = content) 
            comment.save() 
            return redirect(obj.get_absolute_url()) 
    
    else: 
      cf = CommentForm() 

    context ={
        'object': obj,
        'comment_form':cf,
        'comments':comments,
    }
    return render(request, 'detail.html', context)
    

def rate_book(request):
    """rate book"""

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
    username='admin'

    b1 = Book.objects.all()[:10]
        
    b2 = Book.objects.filter(
        score__gte=4).order_by('score')[:8]

    b3 = Book.objects.filter(
            category__category_name=category_name)

    context={
        'best_books_1': b1,
        'best_books_2': b2,
        'best_books_3': b3,
    }
    return render(
        request, "home.html",context
        )


def remove_book(request, book_id):
    """remove book"""

    user = CustomUser.objects.get(
        id=request.user.id
    )
    book_name = Book.objects.get(
        id=book_id
    )
    book = get_object_or_404(
        Book,
        customuser=user,
        book_name=book_name,
    )
    book.delete()

    return redirect('favorite')


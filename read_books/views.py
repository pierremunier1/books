from django.shortcuts import render
from read_books.response import GoogleApi
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
            Book.objects.filter(
                category_name__icontains=request.GET.get('term')
                )[:5] or  
            Book.objects.filter(
                author__icontains=request.GET.get('term')
                )[:5]
            )
        for book in qs:
            books.append(book.product_name)
    return JsonResponse(books, safe=False)

def result(request):
    """show result page"""

    query = request.GET.get('query')

    try:
        book = Book.objects.search_book(query)
    except Book.DoesNotExist:
        messages.info(request, "Book indisponible")
        return redirect("result")

    return render(
        request,
        "home.html",
        {
            "book": book,
        }
    )
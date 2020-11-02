from django.shortcuts import render
from read_books.response import GoogleApi
from django.http import JsonResponse

# Create your views here.

def search(request):
    """autocomplete research in database"""
    
    if request.is_ajax():

        userQuery = request.form["usertext"]
        user_text = GoogleApi.get_books(userQuery)

    return JsonResponse(user_text, safe=False)
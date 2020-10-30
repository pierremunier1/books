from django.shortcuts import render

# Create your views here.

def search(request):
    """showing the home page"""

    return render(request, "home.html")
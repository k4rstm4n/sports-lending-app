from django.shortcuts import render

# Create your views here.

def login_page(request):
    """The landing page for the application"""
    return render(request, 'login/login.html')
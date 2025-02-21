from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout

# Create your views here.


def login_page(request):
    """The landing page for the application"""
    return render(request, "login/login.html")


def index(request):
    return render(request, "login/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


def profile(request):
    return HttpResponse("Hello, world. This is the profile")

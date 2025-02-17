from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'base.html')

def profile(request):
    return HttpResponse("Hello, world. This is the profile")

from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import generic
from .models import Profile

# Create your views here.


def index(request):
    return render(request, "login/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")


def profile(request):
    profile = Profile

    if request.method == 'POST':
        profile.fname = request.POST.get('fname')
        profile.lname = request.POST.get('lname')
        profile.birth_date = request.POST.get('birth_date')
        profile.save()
        ##return redirect() redirect to main page?

    return render(request, 'login/profile.html', {'login/profile': profile})

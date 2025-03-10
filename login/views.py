from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import generic
from .models import Profile
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    return render(request, "login/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")

#class ProfileView(generic.DetailView):
   # model = Profile
  #  template_name = "login/profile.html"

##    def get
    

def profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        profile.fname = request.POST.get('fname')
        profile.lname = request.POST.get('lname')
        profile.birth_date = request.POST.get('birth_date')
        profile.address.address = request.POST.get('address')
        profile.address.city = request.POST.get('city')
        profile.address.state = request.POST.get('state')
        profile.address.zip_code = request.POST.get('zip_code')
        profile.image = request.FILES.get('image')
        profile.save()
        ##return redirect() redirect to main page?

    return render(request, 'login/profile.html', {'profile': profile})

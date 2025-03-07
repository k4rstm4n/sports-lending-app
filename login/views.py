from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views import generic
from .models import Profile
from django.contrib.auth.models import User, Group

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
    is_librarian = profile.user.groups.filter(name='Librarian').exists()
    print(str(profile.user) + " " + str(is_librarian))
    if request.method == 'POST':
        if 'main_submit' in request.POST:
            profile.fname = request.POST.get('fname')
            profile.lname = request.POST.get('lname')
            profile.birth_date = request.POST.get('birth_date')
            profile.address = request.POST.get('address')
            profile.city = request.POST.get('city')
            profile.state = request.POST.get('state')
            profile.zip_code = request.POST.get('zip_code')
            profile.save()
            ##return redirect() redirect to main page?
        elif 'uid_submit' in request.POST:
            uid = request.POST.get('uid')
            other_user = Profile.objects.get(id=uid).user
            
            if other_user is not None:
                patron_group = Group.objects.get(name='Patron')
                librarian_group = Group.objects.get(name='Librarian')
                other_user.groups.add(librarian_group)
                other_user.groups.remove(patron_group)

    return render(request, 'login/profile.html', {'profile': profile, 'is_librarian':is_librarian})

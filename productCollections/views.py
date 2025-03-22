from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Collection
from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User, Permission
from login.models import Profile


# this is for debugging purposes- will probably have to be redone slightly next sprint (just this collection_catalog for viewing)
# if your email is not in collection_private_userlist, dont show it
def collection_catalog(request):
    queryset = Collection.objects.filter()

    context = {"collection_list": queryset}
    return render(request, "productCollections/view_collections.html", context)


class MakeCollectionsCreateView(CreateView):
    model = Collection
    fields = [
        "collection_name",
        "collection_description",
        "collection_privacy",
        "collection_private_userlist",
    ]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        user = self.request.user

        if user.has_perm("login.borrower_perms"):
            form.fields.pop("collection_privacy")
            form.fields.pop("collection_private_userlist")

        elif user.has_perm("login.lender_perms"):
            form.fields["collection_privacy"].choices = (
                Collection.LENDER_PRIVACY_CHOICES
            )

        return form

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.created_at = timezone.now()

        self.object.save()
        if self.request.user.has_perm("login.lender_perms"):
            form.save_m2m()

        return redirect(reverse("productCollections:make_collections"))

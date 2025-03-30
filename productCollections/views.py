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
from django.contrib.auth.mixins import LoginRequiredMixin


def collection_catalog(request):
    form = CollectionFilterForm(request.GET)
    queryset = Collection.objects.all()
    user = request.user

    if form.is_valid():
        if form.cleaned_data["search"]:
            search_query = form.cleaned_data["search"]
            queryset = queryset.filter(
                Q(collection_name__icontains=search_query)
                | Q(collection_description__icontains=search_query)
            )

        if form.cleaned_data["collection_privacy"]:
            queryset = queryset.filter(
                collection_privacy=form.cleaned_data["collection_privacy"]
            )

        context = {
            "form": form,
            "collection_list": queryset,
        }
        return render(request, "productCollections/view_collections.html", context)


class MakeCollectionsCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    fields = [
        "collection_name",
        "collection_description",
        "collection_privacy",
        "collection_private_userlist",
    ]
    # redirect if not logged in
    login_url = "/login/"
    redirect_field_name = "next"

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


def my_collections(request):
    form = CollectionFilterForm(request.GET)

    if request.user.has_perm("login.lender_perms"):
        queryset = Collection.objects.get_queryset()
    elif request.user.has_perm("login.borrower_perms"):
        queryset = Collection.objects.filter(owner=request.user)

    if form.is_valid():
        if form.cleaned_data["search"]:
            search_query = form.cleaned_data["search"]
            queryset = queryset.filter(
                Q(collection_name__icontains=search_query)
                | Q(collection_description__icontains=search_query)
            )

        context = {"form": form, "collection_list": queryset}
        return render(request, "productCollections/catalog.html", context)

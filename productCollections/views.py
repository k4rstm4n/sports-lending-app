from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Collection
from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone


# def make_collections(request):
#     return render(request, "productCollections/make_collections.html")


class MakeCollectionsCreateView(CreateView):
    model = Collection
    fields = [
        "collection_name",
        "collection_description",
        "collection_privacy",
        "collection_creator",
        "collection_private_userlist",
        # "created_at",
    ]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.created_at = timezone.now()
        self.object.save()
        return redirect(reverse("products:product_catalog"))

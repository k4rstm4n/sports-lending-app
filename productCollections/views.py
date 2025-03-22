from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Collection
from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone


# this is for debugging purposes- will probably have to be redone slightly (just this collection_catalog for viewing)
def collection_catalog(request):
    # form = EquipmentFilterForm(request.GET)
    queryset = Collection.objects.filter()

    # if form.is_valid():
    #     if form.cleaned_data['search']:
    #         search_query = form.cleaned_data['search']
    #         queryset = queryset.filter(
    #             Q(name__icontains=search_query) |
    #             Q(description__icontains=search_query) |
    #             Q(brand_icontains=search_query)
    #         )

    #     if form.cleaned_data['category']:
    #         queryset = queryset.filter(category=form.cleaned_data['category'])

    #     if form.cleaned_data['condition']:
    #         queryset = queryset.filter(condition=form.cleaned_data['condition'])

    #     if form.cleaned_data['min_price']:
    #         queryset = queryset.filter(price_per_day__gte=form.cleaned_data['min_price'])

    #     if form.cleaned_data['max_price']:
    #         queryset = queryset.filter(price_per_day__lte=form.cleaned_data['max_price'])

    context = {
        # 'form': form,
        "collection_list": queryset
    }
    return render(request, "productCollections/view_collections.html", context)


class MakeCollectionsCreateView(CreateView):
    model = Collection
    fields = [
        "collection_name",
        "collection_description",
        "collection_privacy",
        # "collection_creator",
        "collection_private_userlist",
        # "created_at",
    ]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.created_at = timezone.now()
        self.object.save()
        return redirect(reverse("products:product_catalog"))

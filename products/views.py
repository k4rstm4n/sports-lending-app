from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Equipment, Review
from .forms import *
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib import messages


# Create your views here.


def product_catalog(request):
    form = EquipmentFilterForm(request.GET)
    queryset = Equipment.objects.filter(is_available=True)

    if form.is_valid():
        if form.cleaned_data["search"]:
            search_query = form.cleaned_data["search"]
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(description__icontains=search_query)
                | Q(brand__icontains=search_query)
            )

        if form.cleaned_data["category"]:
            queryset = queryset.filter(category=form.cleaned_data["category"])

        if form.cleaned_data["condition"]:
            queryset = queryset.filter(condition=form.cleaned_data["condition"])

        if form.cleaned_data["min_price"]:
            queryset = queryset.filter(
                price_per_day__gte=form.cleaned_data["min_price"]
            )

        if form.cleaned_data["max_price"]:
            queryset = queryset.filter(
                price_per_day__lte=form.cleaned_data["max_price"]
            )

        context = {"form": form, "equipment_list": queryset}
        return render(request, "products/catalog.html", context)


class ProductDetailView(generic.DetailView):
    model = Equipment
    template_name = "products/detail.html"

    def get_queryset(self):
        return Equipment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = self.object.reviews.all()  # fetch related reviews
        return context


class ReviewCreate(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "products/review_form.html"
    success_url = reverse_lazy("products:product_catalog")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["equipment"] = Equipment.objects.get(
            pk=self.kwargs["pk"]
        )  # Pass equipment to template
        return data

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user  # Assign user
        self.object.equipment = Equipment.objects.get(
            pk=self.kwargs["pk"]
        )  # Assign equipment
        self.object.created_at = timezone.now()
        self.object.save()
        return super().form_valid(form)


class EquipmentCreateView(CreateView):
    model = Equipment
    fields = [
        "name",
        "description",
        "price_per_day",
        "condition",
        "category",
        "brand",
        "image",
    ]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.created_at = timezone.now()
        self.object.save()
        return redirect(reverse("products:product_catalog"))

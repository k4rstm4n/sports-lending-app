from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Equipment
from .forms import *
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.urls import reverse

# Create your views here.

def product_catalog(request):
    form = EquipmentFilterForm(request.GET)
    queryset = Equipment.objects.filter(is_available=True)

    if form.is_valid():
        if form.cleaned_data['search']:
            search_query = form.cleaned_data['search']
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(brand_icontains=search_query)
            )

        if form.cleaned_data['category']:
            queryset = queryset.filter(category=form.cleaned_data['category'])

        if form.cleaned_data['condition']:
            queryset = queryset.filter(condition=form.cleaned_data['condition'])

        if form.cleaned_data['min_price']:
            queryset = queryset.filter(price_per_day__gte=form.cleaned_data['min_price'])

        if form.cleaned_data['max_price']:
            queryset = queryset.filter(price_per_day__lte=form.cleaned_data['max_price'])

        context = {
            'form': form,
            'equipment_list': queryset
        }
        return render(request, 'products/catalog.html', context)

class EquipmentCreateView(CreateView):
    model = Equipment
    fields = ["name", "description", "price_per_day", "condition", "category", "brand", "image"]

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.created_at = timezone.now()
        self.object.save()
        return redirect(reverse("products:product_catalog"))
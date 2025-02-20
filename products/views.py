from django.shortcuts import render

# Create your views here.

def product_catalog(request):
    return render(request, 'products/catalog.html')
from django.urls import path

from . import views

app_name = "products"

urlpatterns = [

    #products/
    path("", views.product_catalog, name='product_catalog'),

    #products/{productID}
]
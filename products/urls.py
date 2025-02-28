from django.urls import path

from . import views

app_name = "products"

urlpatterns = [

    #products/
    path("", views.product_catalog, name='product_catalog'),

    #products/1/details/
    path("<int:pk>/details/", views.ProductDetailView.as_view(), name='product_detail'),

    #products/{productID}
]
from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("create_equipment/", views.EquipmentCreateView.as_view(), name="create_equipment"),
    #products/
    path("", views.product_catalog, name='product_catalog'),

    #products/1/details/
    path("<int:pk>/details/", views.ProductDetailView.as_view(), name='product_detail'),
    path("<int:pk>/reviews/", views.ReviewCreate.as_view(), name="product_review"),



    #products/{productID}

]
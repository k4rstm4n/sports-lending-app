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
    path("<int:pk>/reviews/edit/", views.ReviewUpdate.as_view(), name="product_review_update"),
    path("<int:equipment_id>/rent/", views.rent_equipment, name="product_rent"),
    path("user/products/", views.my_products, name="my_products"),



    #products/{productID}

]
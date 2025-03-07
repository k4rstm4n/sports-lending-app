from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("create_equipment/", views.EquipmentCreateView.as_view(), name="create_equipment"),
    #products/
    path("", views.product_catalog, name='product_catalog'),

    #products/{productID}

]
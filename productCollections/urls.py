from django.urls import path

from . import views

app_name = "productCollections"

urlpatterns = [
    path(
        "make_collections/",
        views.MakeCollectionsCreateView.as_view(),
        name="make_collections",
    ),
    path("view_collections/", views.collection_catalog, name="view_collections"),
]

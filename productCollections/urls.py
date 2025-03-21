from django.urls import path

from . import views

app_name = "productCollections"

urlpatterns = [
    path(
        "make_collections/",
        views.MakeCollectionsCreateView.as_view(),
        name="make_collections",
    ),
    # path("make_collections/", views.make_collections, name="make_collections"),
]

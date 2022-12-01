from django.urls import path
from .views import Logout, Index, PlacesListView, PlacesCreateView, PlacesUpdateView

urlpatterns = [
    path("", Index.as_view(), name="hello"),
    path("logout/", Logout.as_view(), name="logout"),
    path("list/", PlacesListView.as_view(), name="list"),
    path("add/", PlacesCreateView.as_view(), name="add"),
    path("place/<int:pk>/", PlacesUpdateView.as_view(), name="view_place"),
]

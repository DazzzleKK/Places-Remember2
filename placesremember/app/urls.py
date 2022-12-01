from django.urls import path
from .views import Logout, Index, PlacesListView, PlacesCreateView

urlpatterns = [
    path("", Index.as_view(), name="hello"),
    path("logout/", Logout.as_view(), name="logout"),
    path("list/", PlacesListView.as_view(), name="list"),
    path("add/", PlacesCreateView.as_view(), name="add"),
]

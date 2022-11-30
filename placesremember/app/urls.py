from django.urls import path
from .views import Logout, Index

urlpatterns = [
    path("", Index.as_view(), name="hello"),
    path("logout/", Logout.as_view(), name="logout"),
]

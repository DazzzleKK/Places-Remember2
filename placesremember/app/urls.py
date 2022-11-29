from django.urls import path
from .views import hello, Logout

urlpatterns = [
    path("", hello, name="hello"),
    path("logout/", Logout.as_view(), name="logout"),
]

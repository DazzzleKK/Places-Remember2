from django.shortcuts import render
from django.contrib.auth.views import LogoutView

# Create your views here.


def hello(request):
    return render(request, "app/hello.html")


class Logout(LogoutView):
    template_name = "app/hello.html"

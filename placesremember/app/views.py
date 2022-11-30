from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView

# Create your views here.


class Index(TemplateView):
    template_name = "app/index.html"


class Logout(LogoutView):
    template_name = "app/index.html"

from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import Places

# Create your views here.


class Index(TemplateView):
    template_name = "app/index.html"


class Logout(LogoutView):
    template_name = "app/index.html"


class PlacesListView(ListView):
    model = Places
    template_name = "app/list.html"
    context_object_name = "places"

    def get_queryset(self):
        if self.request.user.username:
            return Places.objects.filter(user=self.request.user)
        else:
            return None

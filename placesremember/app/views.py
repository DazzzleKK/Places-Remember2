from django.contrib.auth.views import LogoutView
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .forms import NewPlaceForm, PlacesDetailForm
from .models import Places

# Create your views here.


class Index(TemplateView):
    template_name = "app/index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("list")
        return super().dispatch(request, *args, **kwargs)


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


class PlacesCreateView(CreateView):
    form_class = NewPlaceForm
    template_name = "app/new_place.html"
    success_url = reverse_lazy("list")

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(PlacesCreateView, self).form_valid(form)


class PlacesUpdateView(UpdateView):
    model = Places
    form_class = PlacesDetailForm

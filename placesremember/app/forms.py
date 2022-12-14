from django import forms
from .models import Places
from django.contrib.gis.forms import OSMWidget


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ["name", "description", "location"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Новое место"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "(необязательно)",
                }
            ),
            "location": OSMWidget(attrs={"map_width": 350,}),
        }


class PlacesDetailForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ["name", "description", "location"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "disabled": None}),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "disabled": None,
                }
            ),
            "location": OSMWidget(attrs={"map_width": 350,}),
        }

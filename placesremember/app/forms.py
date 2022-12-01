from django import forms
from .models import Places
from mapwidgets.widgets import GooglePointFieldWidget


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
            "location": GooglePointFieldWidget,
        }

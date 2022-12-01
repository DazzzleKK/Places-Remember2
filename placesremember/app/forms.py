from django import forms
from .models import Places
from mapwidgets.widgets import GooglePointFieldWidget


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ["name", "desctiption", "location"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Новое место"}
            ),
            "desctiption": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "(необязательно)",
                }
            ),
            "location": GooglePointFieldWidget,
        }

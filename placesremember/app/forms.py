from django import forms
from .models import Places
from mapwidgets.widgets import GooglePointFieldWidget  # GoogleStaticOverlayMapWidget


class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Places
        fields = ["name", "latitude", "longitude", "location"]
        widgets = {"location": GooglePointFieldWidget}

# from django.contrib import admin
from .models import Profile, Places
from django.contrib.gis import admin

admin.site.register(Profile)


@admin.register(Places)
class PlacesAdmin(admin.OSMGeoAdmin):
    list_display = ("name", "location")

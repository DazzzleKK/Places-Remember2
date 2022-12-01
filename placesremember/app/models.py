from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField


class Places(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location = PointField(null=True)

    def __str__(self):
        return f"Место :{self.name} Автор: {self.user} Локация: {self.latitude} {self.longitude}"


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    avatar = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.gis.db.models import PointField
from django.urls import reverse


class Places(models.Model):
    name = models.CharField(verbose_name="Название", max_length=150)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    description = models.CharField(verbose_name="Описание", max_length=300, null=True)
    location = PointField(verbose_name="Место", null=True)

    def __str__(self):
        return f"Место :{self.name} Автор: {self.user}"

    def get_absolute_url(self):
        return reverse("view_place", kwargs={"pk": self.pk})


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    avatar = models.CharField(max_length=300, null=True, blank=True)

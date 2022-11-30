from django.db import models

# from django.conf import settings
from django.contrib.auth.models import User


# class Places(models.Model):
#     name = models.CharField(max_length=150)
#     author = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
#     )
#     # place_location = models.PointField()


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    avatar = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} Profile"

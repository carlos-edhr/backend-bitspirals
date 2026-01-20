from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    company = models.CharField(max_length=350, blank=True, null=True)
    position = models.CharField(max_length=350, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.username}"

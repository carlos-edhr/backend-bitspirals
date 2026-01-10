from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    tittle = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Ordena las notas por la más reciente primero
        ordering = ["-created_at"]

    def __str__(self):
        return self.tittle

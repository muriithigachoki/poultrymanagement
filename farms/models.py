from django.db import models
from django.contrib.auth.models import User


class Farm(models.Model):
    farmer = models.ForeignKey(User, on_delete=models.CASCADE)
    farmName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.farmName

    class Meta:
        ordering = ["created_at"]

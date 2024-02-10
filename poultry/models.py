from django.db import models
from farms.models import Farm


class Poultry(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    age_in_weeks = models.PositiveIntegerField()
    no_of_poultries = models.PositiveIntegerField()
    breed = models.CharField(max_length=50)
    date_add = models.DateField(auto_now_add=True)
    description = models.TextField(default=True)

    def __str__(self):
        return self.breed

    class Meta:
        ordering = ["date_add"]

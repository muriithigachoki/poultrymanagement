from django.db import models
from farms.models import Farm


class IncomeSource(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Income(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    source = models.ForeignKey(IncomeSource, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.source} Income - ${self.amount}"

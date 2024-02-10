from django.db import models
from farms.models import Farm


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Expense(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    expense_date = models.DateField()
    description = models.CharField(max_length=2000)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.description[0:50]

    class Meta:
        ordering = ["created_at"]

    def save(self, *args, **kwargs):
        self.month = self.expense_date.month
        self.year = self.expense_date.year
        return super().save(*args, **kwargs)

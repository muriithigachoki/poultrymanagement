from django.urls import path
from . import views

urlpatterns = [
    path("<int:farm_id>/", views.income_list, name="income-list"),
    path("add/", views.add_income, name="add-income"),
]

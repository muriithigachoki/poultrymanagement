from django.urls import path
from . import views

urlpatterns = [
    path("farm/<int:farm_id>/expense/", views.expense_list, name="expense-list"),
    path("farm/expense/add/", views.add_expense, name="create-expense"),
    path("farm/<int:farm_id>/expense/<int:pk>/", views.expense_detail, name="expense-detail"),
]


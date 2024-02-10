from django.urls import path
from . import views

urlpatterns = [
    path("farms/<int:farm_id>/poultries/", views.poultry_list, name="poultry-list"),
    path("farms/poultries/add/", views.add_poultry, name="create-poultry"),
    path("farms/<int:farm_id>/poultries/<int:pk>/", views.poultry_detail, name="poultry-detail"),
]

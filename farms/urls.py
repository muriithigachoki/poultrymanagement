from django.urls import path
from . import views

urlpatterns = [
    path("", views.farm_list, name="farm-list"),
    path("<int:pk>/", views.farm_detail, name="farm-detail"),
    path("createfarm/", views.createFarm, name="createfarm"),
    path("update-farm/<int:pk>/", views.updateFarm, name="update-farm"),
    path("delete-farm/<int:pk>/", views.deleteFarm, name="delete-farm"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerPage, name="register"),
]

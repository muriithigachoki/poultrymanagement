from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from farms.forms import FarmForm
from django.db.models import Q
from .models import Farm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


@login_required(login_url="login")
def farm_list(request):
    q = request.GET.get("q") if request.GET.get("q") != None else ""

    farms = Farm.objects.filter(Q(farmName__icontains=q) | Q(description__icontains=q))

    farm_count = farms.count
    context = {"farms": farms, "farm_count": farm_count}
    return render(request, "farms/farm_list.html", context)

@login_required(login_url="login")
def farm_detail(request, pk):
    farm = get_object_or_404(Farm, pk=pk)
    context = {"farm": farm}
    return render(request, "farms/farm_detail.html", context)


@login_required(login_url="login")
def createFarm(request):
    form = FarmForm()

    if request.method == "POST":
        form = FarmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("farm-list")
    context = {"form": form}
    return render(request, "farms/farm_form.html", context)


@login_required(login_url="login")
def updateFarm(request, pk):
    farm = get_object_or_404(Farm, pk=pk)

    if request.user != farm.farmer:
        return HttpResponse("you are not allowed here")

    if request.method == "POST":
        form = FarmForm(request.POST, instance=farm)
        if form.is_valid():
            form.save()
            return redirect("farm-list")
    else:
        form = FarmForm(instance=farm)

    context = {"form": form}
    return render(request, "farms/farm_form.html", context)


@login_required(login_url="login")
def deleteFarm(request, pk):
    farm = Farm.objects.get(id=pk)

    if request.user != farm.farmer:
        return HttpResponse("you are not allowed here")

    if request.method == "POST":
        farm.delete()
        return redirect("farm-list")
    context = {"obj": farm}
    return render(request, "farms/delete.html", context)


def loginPage(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "user does not exist")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("farm-list")
        else:
            messages.error(request, "username or password does not exit")

    context = {"page": page}
    return render(request, "farms/login_register.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


def registerPage(request):
    form = CustomUserCreationForm()  # Use the custom form

    if request.user.is_authenticated:
        return redirect("farm-list")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data[
                "username"
            ]  
            user.save()
            login(request, user)
            messages.success(
                request, "Registration successful"
            )  
            return redirect("farm-list")
        else:
            messages.error(request, "An error occurred during registration")
    context = {"form": form}
    return render(request, "farms/login_register.html", context)

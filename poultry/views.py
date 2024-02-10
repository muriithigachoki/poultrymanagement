from django.shortcuts import render, redirect, get_object_or_404
from .models import Poultry
from django.contrib.auth.decorators import login_required
from .forms import PoultryForm
from django.http import HttpResponse

@login_required(login_url="login")
def poultry_list(request, farm_id):
    poultries = Poultry.objects.filter(farm_id=farm_id)    
    context = {"poultries": poultries}
    return render(request, "poultry/poultry_list.html", context)

@login_required(login_url="login")
def poultry_detail(request, farm_id, pk):
    poultry = get_object_or_404(Poultry, farm_id=farm_id, pk=pk)

    if request.farm_id != poultry.farm_id:
        return HttpResponse("you are not allowed here")
    
    context = {"poultry": poultry}
    return render(request, "poultry/poultry_list.html", context)


@login_required(login_url="login")
def add_poultry(request):
    form = PoultryForm()
    if request.method == "POST":
        form = PoultryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("farm-list")
    context = {"form": form}
    return render(request, "poultry/poultry_form.html", context)

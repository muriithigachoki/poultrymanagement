from django.shortcuts import render, redirect
from .models import Income
from .forms import IncomeForm
from django.contrib.auth.decorators import login_required


def income_list(request, farm_id):
    # Get all incomes for the specified farm
    incomes = Income.objects.filter(farm_id=farm_id)
    context = {"incomes": incomes}
    return render(request, "income/income-list.html", context)


@login_required(login_url="login")
def add_income(request):
    form =IncomeForm()
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense-list")
    context = {"form": form}
    return render(request, "income/income_form.html", context)

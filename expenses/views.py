from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from expenses.models import Expense
from expenses.forms import ExpenseForm


def expense_list(request, farm_id):
    expense = Expense.objects.filter(farm_id=farm_id)
    context = {"expense": expense}
    return render(request, "expenses/expense_list.html", context)


def expense_detail(request, farm_id, pk):
    expense = get_object_or_404(Expense, farm_id=farm_id, pk=pk)
    context = {"expense": expense}
    return render(request, "expenses/expense_detail.html", context)



@login_required(login_url="login")
def add_expense(request):
    form =ExpenseForm()
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense-list")
    context = {"form": form}
    return render(request, "expenses/expense_form.html", context)
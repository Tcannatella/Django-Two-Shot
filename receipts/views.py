from django.shortcuts import render, redirect
from receipts.models import Receipt, ExpenseCategory, Account
from receipts.forms import ReceiptForm
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def receipts_list(request):
    item = Receipt.objects.filter(purchaser=request.user)
    context = {
        "receipts_list": item,
    }

    return render(request, "receipts/list.html", context)

@login_required
def create_receipt(request):
    if request.method == "POST":
        form = ReceiptForm(request.POST)
        if form.is_valid():
            receipt = form.save(False)
            receipt.purchaser = request.user
            receipt.save()
            return redirect("home")
    else:
        form = ReceiptForm()

    context = {
        "form": form,
    }
    return render(request, "receipts/create.html", context)


@login_required
def category_list(request):
    item = ExpenseCategory.objects.filter(owner=request.user)
    context = {
        "category_list": item,
    }

    return render(request, "receipts/categories.html", context)

@login_required
def account_list(request):
    item = Account.objects.filter(owner=request.user)
    context = {
        "account_list": item,
    }

    return render(request, "receipts/accounts.html", context)

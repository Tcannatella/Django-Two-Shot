from django.shortcuts import render, get_object_or_404, redirect
from receipts.models import Receipt

# Create your views here.

def receipts_list(request):
    item = Receipt.objects.all()
    context = {
        "receipts_list" : item,
    }

    return render(request, "receipts/list.html", context)



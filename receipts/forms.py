from django.forms import ModelForm
from receipts.models import Receipt, ExpenseCategory


class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields = [
            "vendor",
            "total",
            "date",
            "tax",
            "category",
            "account",
        ]

class ExpenseCategoryForm(ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = [
          "name"
        ]
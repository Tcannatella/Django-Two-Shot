from django.urls import path
from receipts.views import receipts_list, create_receipt

urlpatterns = [
    path("create/", create_receipt, name="create_receipt"),
    path("", receipts_list, name="home" )
]

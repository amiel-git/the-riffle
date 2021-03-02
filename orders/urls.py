from django.urls import path
from .views import updateItem

app_name = "orders"

urlpatterns = [
    path('update-item/',updateItem,name="update-item"),
]

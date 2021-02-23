from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('all/',views.ProductsListView,name='list'),
    path('add-product/',views.CreateProductView,name='create'),
]

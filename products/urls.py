from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('all/',views.ProductsListView,name='list'),
    path('add-product/',views.CreateProductView,name='create'),
    path('<int:pk>/',views.ProductDetailView.as_view(),name='detail'),
    path('<int:pk>/update',views.ProductUpdateView.as_view(),name='update'),
    path('<int:pk>/delete',views.ProductDeleteView.as_view(),name='delete'),
    path('shop/',views.ShopView.as_view(),name="shop"),
]
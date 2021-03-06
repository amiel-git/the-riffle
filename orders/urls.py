from django.urls import path
from .views import updateItem,CheckoutViewStep1,CheckoutViewStep2, PaymentSuccessView,PaymentCancelledView

app_name = "orders"

urlpatterns = [
    path('update-item/',updateItem,name="update-item"),
    path('checkout-address/',CheckoutViewStep1.as_view(),name="checkout1"),
    path('charge/',CheckoutViewStep2.as_view(),name='charge'),
    path('success/',PaymentSuccessView.as_view(),name="success"),
    path('cancel/',PaymentCancelledView.as_view(),name="cancel"),
]

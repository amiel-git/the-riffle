from django.contrib import admin
from accounts.models import Profile
from products.models import Product
from orders.models import Order, OrderItem
# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
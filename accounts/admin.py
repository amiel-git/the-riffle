from django.contrib import admin
from accounts.models import Profile
from products.models import Product
# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
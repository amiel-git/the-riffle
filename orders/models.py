from django.db import models

from products.models import Product
from accounts.models import Profile


class Order(models.Model):

    user = models.ForeignKey(
        Profile,
        related_name = "orders",
        on_delete=models.SET_NULL,
        null = True
    )
    date_ordered = models.DateTimeField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    shipping_address = models.CharField(max_length=255)

    
    def __str__(self):
        return self.id
    


class OrderItem(models.Model):

    product = models.ForeignKey(
        Product,
        related_name = "order_item",
        on_delete = models.CASCADE
    )

    order = models.ForeignKey(
        Order,
        related_name = "order_item",
        on_delete= models.CASCADE
    )

    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.id
    

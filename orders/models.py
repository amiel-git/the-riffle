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
    shipping_address = models.TextField(max_length=255)
    delivered = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id}"
    

    @property
    def get_items_total(self):
        total = sum([item.get_total for item in self.order_item.all()])
        return total

    @property
    def get_number_of_items(self):
        orderitems = self.order_item.all()
        total = sum([item.quantity for item in orderitems])
        return total



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
        return f"{self.id}"
    

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
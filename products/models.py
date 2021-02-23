from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    stocks = models.IntegerField(default=0)
    product_image = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.name
    
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json

from products.models import Product
from orders.models import Order,OrderItem

def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    product = Product.objects.get(id=product_id)

    order, created = Order.objects.get_or_create(user=request.user, is_complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "delete":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)
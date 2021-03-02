from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json

from products.models import Product
from orders.models import Order

def updateItem(request):
    data = json.loads(request.body)
    product_id = int(data['productId'])
    action = data['action']

    return JsonResponse("Item was added", safe=False)
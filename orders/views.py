from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json

from products.models import Product
from orders.models import Order,OrderItem

from django.views import View

from django.http import HttpResponseRedirect,JsonResponse
from django.urls import reverse

import stripe
import os
stripe.api_key = os.environ['stripe_api_key']


def updateItem(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']
    product = Product.objects.get(id=product_id)

    order, created = Order.objects.get_or_create(user=request.user, is_complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)



class Cart(View):

    template_name = "shop/cart.html"

    def get(self,request):

        order, created = Order.objects.get_or_create(user=request.user,is_complete=False)
        items = order.order_item.all()

        return render(request,self.template_name,context={
            "items":items,
            "order":order,
        })


class CheckoutViewStep1(View):

    template_name = "shop/checkout_step1.html"

    def post(self,request):
        
        shipping_address = request.POST.get('shipping_address')
        order = Order.objects.get(user=request.user, is_complete=False)

        order.shipping_address = shipping_address

        order.save()

        return HttpResponseRedirect(reverse('orders:charge')) # Temporary will change this to step2

    def get(self,request):
        order = Order.objects.get(user=request.user, is_complete=False)
        context = {'order':order}
        return render(request,self.template_name,context=context)



class CheckoutViewStep2(View):
    

    def post(self,request,*args,**kwargs):
        order = Order.objects.get(user=request.user, is_complete=False)
        raw_items = order.order_item.all()
        items = []
        for item in raw_items:
            items.append(
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.product.price * 100,
                        'product_data': {
                            'name': item.product.name,
                        },
                    },
                    'quantity': item.quantity,
                    
                }
            )

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=items,
            mode='payment',
            success_url= "http://127.0.0.1:8000/orders/success/",
            cancel_url= "http://127.0.0.1:8000/orders/cancel/",
        )

        return JsonResponse({'id': checkout_session.id})

    def get(self,request,*args,**kwargs):
        order = Order.objects.get(user=request.user, is_complete=False)
        items = order.order_item.all()
        return render(request,"shop/checkout_step2.html",{"order":order,"items":items})
        


class PaymentSuccessView(View):

    template_name = "shop/success.html"
    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)

    

class PaymentCancelledView(View):

    template_name = "shop/cancelled.html"
    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)
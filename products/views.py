from django.shortcuts import render

from products.models import Product
from products.forms import ProductForm

from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse, reverse_lazy


## PRODUCTS CRUD views (For staff members only) ##

def ProductsListView(request):

    products = Product.objects.all()

    return render(request,'products/products-list.html',context={'products':products})


def CreateProductView(request):
    """
    Views to create/add new products
    """
    form = ProductForm()

    if request.method == "POST":

        form = ProductForm(request.POST,request.FILES)
        print(request.FILES)
        if form.is_valid():
            product = form.save(commit=False)

            if 'product_image' in request.FILES:
                product.product_image = request.FILES.get('product_image')
                product.save()           
            else:
                product.save()

            return HttpResponseRedirect(reverse('products:list'))

        else:
            return HttpResponse(form.errors)

    return render(request,'products/add-product.html',context={'form':form})



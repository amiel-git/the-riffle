from django.shortcuts import render
from django.core import serializers

from django.views import generic,View

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


class ProductDetailView(generic.DetailView):

    model = Product
    context_object_name = "product_detail"
    template_name = "products/product-detail.html"


class ProductUpdateView(generic.UpdateView):

    model = Product
    template_name = "products/add-product.html"
    form_class = ProductForm
    context_object_name = "product"


class ProductDeleteView(generic.DeleteView):

    model = Product
    success_url = reverse_lazy('products:list')



## Products view for customers

class ShopView(View):

    template_name = "shop/shop.html"
    def get(self,request,*args, **kwargs):
        products = Product.objects.all().order_by("date_added")

        return render(request,self.template_name,{
            "products": products
        })
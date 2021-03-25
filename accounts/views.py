from django.shortcuts import render
from accounts.forms import RegistrationForm

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import login,authenticate,logout

from products.models import Product

def index(request):
    latest_products = Product.objects.all().order_by("-date_added")[:6]
    return render(request,'core/index.html', context={"products":latest_products})


def RegistrationView(request):
    """
    This view handles the creation of new site users (Regular users)
    """
    registration_form = RegistrationForm()

    if request.method == "POST":

        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponse(
                registration_form.errors,
            )

    return render(request,'accounts/register.html',context={'form':registration_form})


def loginview(request):
    
    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email,password=password)

        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request,'accounts/login.html',context={"failed":True})
        
    return render(request,'accounts/login.html')


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
        




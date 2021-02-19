from django.contrib import admin
from django.urls import path,include
from accounts.views import index,loginview,logoutview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login/',loginview,name='login'),
    path('logout',logoutview,name='logout'),
    path('accounts/',include('accounts.urls')),
    
]

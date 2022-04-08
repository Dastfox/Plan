"""Planningator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from planning_app.views import delete, index_app, redirection
from accounts.views import Error, index_acc, thanks, already, about


urlpatterns = [
    path('', redirection , name= 'index'),
    path('take_me_to_internet', index_app, name= 'index_app'),
    path('new',index_acc, name= 'index_acc'),
    path('thanks',thanks, name='thanks'),
    path('admin/', admin.site.urls),
    path('error', Error, name= 'error',),
    path('already', already ,name = "already"),
    path('deletetheuniverse',delete,name = 'delete',),
    path('about',about,name = 'about'),
]

from distutils.log import error
from logging import exception
from tabnanny import check
from typing import Counter
from urllib import response
from venv import create
from wsgiref import validate
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import NewUrlForm
from urllib.parse import urljoin
from .models import Random_Link
from django.urls import resolve, Resolver404
import requests
from django.core.validators import URLValidator
from accounts.models import Random_Link, entry_list
import random




def index_acc(request):
    if request.method != 'POST':
        entry_list = list (Random_Link.objects.all())
        compteur =  len(entry_list)       
        return render(request, 'accounts/index.html', 
                      context = {"C": compteur})
        
    URL = request.POST.get("URL")
    validate = URLValidator()
    
    try:
        validate(URL)
        try:
            response = requests.get(URL)
            random_link, created = Random_Link.objects.get_or_create(link=URL)
            if created:
                random_link.save()
                return redirect(thanks)
            else: already
            return redirect(already)
        except requests.ConnectionError as exception:
            return redirect(already)       
    except ValidationError as exception:
        return redirect (Error)

def thanks (request):
    entry_list = list(Random_Link.objects.all())
    compteur =  len(entry_list)       
    return render(request,'accounts/thanks.html',context = {"C": compteur})

def Error (request):
    entry_list = list(Random_Link.objects.all())
    compteur =  len(entry_list)       
    return render(request,'accounts/Error.html',context = {"C": compteur})

def already (request):
    entry_list = list(Random_Link.objects.all())
    compteur =  len(entry_list)       
    return render(request,'accounts/already.html',context = {"C": compteur})
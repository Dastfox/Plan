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
import httplib2 
from urllib.parse import urljoin
from .models import Random_Link
from django.urls import resolve, Resolver404
import requests
from django.core.validators import URLValidator
# Create your views here.
# def get_url(request):
#     if request.method == 'POST':
#         form = NewUrlForm(request.POST)
#         if form.is_valid():
#              return HttpResponseRedirect('/thanks/')
#     else:
#         form = NewUrlForm()
#     return render(request,'URL.html')




def index_acc(request):
    if request.method != 'POST':
        return render(request, 'accounts/index.html')
    URL = request.POST.get("URL")
    validate = URLValidator()
    
    try:
        validate(URL)
        try:
            response = requests.get(URL)
            random_Link, created = Random_Link.objects.get_or_create(link=URL)
            if created:
                random_Link.save()
            else: thanks
            return redirect(thanks)
        except requests.ConnectionError as exception:
            return redirect(thanks)       
    except ValidationError as exception:
        return redirect (thanks)

        
        
    

def thanks (request):
    return render(request,'accounts/thanks.html')
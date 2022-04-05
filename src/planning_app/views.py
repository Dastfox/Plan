from multiprocessing import context
import random
from django.shortcuts import redirect, render
from django.db.models import Max, Min, Count
from django.db import  models  
from accounts.models import Random_Link, entry_list
from django.contrib.auth import get_user_model,login, logout, authenticate

User = get_user_model

def index_app(request):   
    random_link = random.choice(Random_Link.objects.all())
    entry_list = list (Random_Link.objects.all())
    compteur =  len(entry_list)
    return render(request, 'planning_app/index.html',context={"Q": random_link.link, "C": compteur})

def delete(request): 
    random_link = random.choice(Random_Link.objects.all())
    entry_list = list (Random_Link.objects.all())
    compteur =  len(entry_list)
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(username=username, password=password):
            login(request, user)
            to_delete = Random_Link.objects.all()
            to_delete.delete()
            random_link, created = Random_Link.objects.get_or_create(link='https://fr.wikipedia.org/wiki/Julien_Lepers')
            return redirect('index_app')

    return render(request,'planning_app/DEL.html',context={"C": compteur})

def redirection (request):
    return redirect ('index_app')


       

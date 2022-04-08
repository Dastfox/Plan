from multiprocessing import context
import random
from django.shortcuts import redirect, render
from django.db import  models  
from accounts.models import Random_Link, entry_list
from django.contrib.auth import get_user_model,login, logout, authenticate




def index_app(request):   
    random_link = random.choice(Random_Link.objects.all())
    entry_list = list (Random_Link.objects.all())
    compteur =  len(entry_list)
    return render(request, 'planning_app/index.html',
                  context={"Q": random_link.link, 
                           "C": compteur,
                           "O": "new", 
                           "Label": "Ajouter un truc à l'internet?"})

User = get_user_model

def delete(request): #vue suppression SQLite
    random_link = random.choice(Random_Link.objects.all()) #choix aléatoire d'un objet dans models
    entry_list = list (Random_Link.objects.all()) #compteur
    compteur =  len(entry_list)
    if request.method == 'POST': 
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(username=username, password=password):
            login(request, user)
            to_delete = Random_Link.objects.all() #supprime tout
            to_delete.delete()
            random_link, created = Random_Link.objects.get_or_create(link='https://fr.wikipedia.org/wiki/Julien_Lepers') #ajoute 1 lien pour éviter SQlite vide
            return redirect('index_app')

    return render(request,'planning_app/DEL.html',context={"C": compteur ,"O": 'take_me_to_internet'})

def redirection (request): #redirection url vide après l'appli vers teke me to internet
    return redirect ('index_app')


       

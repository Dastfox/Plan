
from django.forms import ValidationError
from django.shortcuts import redirect, render
from .models import Random_Link
import requests
from django.core.validators import URLValidator
from accounts.models import Random_Link, entry_list
from planning_app.views import index_app


#Page d'index > Ajout de liens
def index_acc(request):
    if request.method != 'POST':
        #compteur
        entry_list = list (Random_Link.objects.all())
        compteur =  len(entry_list)       
        # C = compteur O = lien du bouton du footer Label = label de celui-ci
        return render(request, 'accounts/index.html', 
                      context = {"C": compteur, 
                                 "O": "take_me_to_internet", 
                                 "Label": "Naviguer dans l'internet?"})
    #validateur    
    URL = request.POST.get("URL")
    validate = URLValidator()
    
    try:
        validate(URL)
        try:
            response = requests.get(URL)
            random_link, created = Random_Link.objects.get_or_create(link=URL)
            if created: #Objet créé
                random_link.save()
                return redirect(thanks)
            else: already
            return redirect(already)
        except requests.ConnectionError as exception:
            return redirect(already)       
    except ValidationError as exception:
        return redirect (Error)

def thanks (request): #Vue "thanks" + compteur
    entry_list = list(Random_Link.objects.all())
    compteur =  len(entry_list)       
    return render(request,'accounts/thanks.html',context = {"C": compteur,"O": "new", "Label": "Retour"})

def Error (request):#Vue "error" + compteur
    entry_list = list(Random_Link.objects.all())
    compteur =  len(entry_list)       
    return render(request,'accounts/Error.html',context =  {"C": compteur,"O": "new", "Label": "Retour"})

def already (request):#Vue "already added" + compteur
    entry_list = list(Random_Link.objects.all())
    compteur =  len(entry_list)       
    return render(request,'accounts/already.html',context =  {"C": compteur,"O": "new", "Label": "Retour"})

def about (request):#Vue "about" + compteur
    entry_list = list(Random_Link.objects.all())
    compteur =  len(entry_list)       
    return render(request,'accounts/about.html',context =  {"C": compteur,"O": "take_me_to_internet", "Label": "Retour"})
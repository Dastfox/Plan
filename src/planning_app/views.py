import random
from django.shortcuts import redirect, render
from django.db.models import Max, Min
from django.db import  models  
from accounts.models import Random_Link
# Create your views here.

# def get_id(self,id):
#     return self.id

def index_app(request):   
    maxi = Random_Link.objects.aggregate(max=Max(id,output_field= models.FloatField()))
    # if request.method != 'POST':
    #     return render(request, 'planning_app/index.html')
    # else:
    RandomSeed = random.randint(1,maxi)
    random_link = Random_Link.get(id=RandomSeed)
    Query = random_link.link
    return render(request, 'planning_app/index.html')
    
    
    
    # return render(request, 'planning_app/index.html')




    
    


def redirection (request):
    return redirect ('index_app')


       

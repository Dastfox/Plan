from pyexpat import model
from typing import Counter
from unicodedata import name
from django.db import models
# Create your models here.



class Random_Link(models.Model):
        link = models.TextField(max_length=2300)
        Counter = models.IntegerField
        def __str__(self):
                return self.Counter
        
# class Counter(models.Model):
#     def __init__(self, Cnumber):
#         self.Cnumber = models.IntegerField(default=2)
                                        

       
    

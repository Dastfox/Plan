from importlib.metadata import entry_points
from pyexpat import model
from typing import Counter
from unicodedata import name
from django.db import models
# Create your models here.



class Random_Link(models.Model):
        link = models.TextField(max_length=2300)    
        def __str__(self):
                return self.link
        
    

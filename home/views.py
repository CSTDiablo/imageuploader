from pyexpat import model
from django.shortcuts import render
from .models import Image
from django.views.generic import ListView

# Create your views here.


class IndexPageView(ListView):
    model=Image
    template_name='home/index.html'
    context_object_name ='items'
    
    

from django.shortcuts import render
from .models import Project, Databases, Lenguajes, Complements

# Create your views here.

def home(request):
    proyectos= Project.objects.all()
    lenguajes= Lenguajes.objects.all()
    databases= Databases.objects.all()
    complements= Complements.objects.all()
    
    return render(request, 'home.html',{
    'proyectos': proyectos, 
    'lenguajes':lenguajes , 
    'databases':databases , 
    'complements':complements
    }
    )
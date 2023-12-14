from tasks.models import Collection, Task
from django.shortcuts import render
from django.utils.html import escape
from django.http import HttpResponse
from yeelight import Bulb

# Create your views here.

def index(request):
    
    context = {}
    collection = Collection.get_default_collection()
    context["collections"] = Collection.objects.order_by("slug")
    
    return render(request,'task/index.html',context=context)


def add_collection(request):
    
    collection_name = escape(request.POST.get("collection-name")) # Escape permet d'empêcher "l'exécution" de caractères spéciaux. (éviter à l'utilisateur de faire des trucs dangereux)
    collection, created = Collection.objects.get_or_create(name = collection_name)
    if not created: 
        return HttpResponse("La collection existe déjà", status = 409) # Status code "exist already" 409 conflict

    return HttpResponse(f'<h2>{collection_name}</h2>')


def add_task(request):
    collection = Collection.get_default_collection()
    
    description = escape(request.POST.get("task-description"))
    Task.object.create(description = description, collection = collection)
    
    return HttpResponse(description)



'''
def connect_iot(request):

    try:
        # Remplacer l'adresse IP ci-dessous par l'adresse IP de votre ampoule Yeelight
        ampoule = Bulb("192.168.1.58")
        ampoule.turn_on()
        return HttpResponse("Lumière allumée avec succès !")
    except Exception as e:
        return HttpResponse(f"Erreur : {e}")
'''



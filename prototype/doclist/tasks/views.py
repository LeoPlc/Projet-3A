from django.shortcuts import render
from django.http import HttpResponse
from yeelight import Bulb

# Create your views here.

def index(request):
    return render(request,'tasks/index.html',context={})

def connect_iot(request):
    try:
        # Remplacer l'adresse IP ci-dessous par l'adresse IP de votre ampoule Yeelight
        ampoule = Bulb("192.168.1.58")
        ampoule.turn_on()
        return HttpResponse("Lumière allumée avec succès !")
    except Exception as e:
        return HttpResponse(f"Erreur : {e}")

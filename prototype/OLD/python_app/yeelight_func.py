<<<<<<< Updated upstream
import yeelight
import func 
import tkinter as tk
import tkinter.messagebox


'''
Besoin d'une nouvelle variable permettant de prendre en compte l'objet auquel on souhaite se connecter. Plus encore, 
il faudrait faire en sorte de pouvoir choisir ultérieurement à la découverte des IoT disponibles, qu'il faudrait insérer 
plutôt directement dans la liste au lieu d'avoir une nouvelle fenêtre. Idée: udpate_iot_list() une fois les appareils découverts
en y intégrant non pas l'adresse IP mais plutôt le nom associé à l'appareil, avec un bouton permettant d'avoir toute une liste d'informations
à propos de l'objet disponible (état, température humidité, etc...).
'''

#recherche d'IoT disponibles (ici bulbes pour la librairie yeelight pour les démo)

def lookfor_available_bulbs(available_bulbs):
    # available_bulbs = yeelight.discover_bulbs()
    available_bulbs= "hello"
    if not available_bulbs:
        tkinter.messagebox.showinfo("ERROR","No available bulb")
    else: 
        bulbs_window = tk.Tk()
        bulbs_window.title("Available bulbs:")
        bulbs_window.geometry("200x300")
        
        bulbs_window.mainloop()
        
def connect_available_bulb():
    #choix du bulbe
    
    #connexion à au bulbe choisi
    
    #choix de l'action à y faire
=======
>>>>>>> Stashed changes

from yeelight import discover_bulbs, Bulb
import readline

import yeelight_connexion as yc

import tkinter as tk

from tkinter import PhotoImage



# Lampe Xiaomi Mathis
# 192.168.1.58

# Constants definition
montrerIPdispo = 1
connexionIPchoisie = 2
allumerLampe = 3
eteindreLampe = 4
lancerDemo = 5


# Variables globales

ipAddr = None
object = None



def choixFunction():
    print("Options disponibles :\n'1': addresses IP disponibles\n'2': se connecter à une addresse IP\n'3':Allumer l'appareil.\n'4':Eteindre l'appareil connecté.\n'5': lancer la démo\n")
    choix = input("Choisissez une option: \n")    
    print("votre choix:", choix)
    return choix

def choix1ipDisponibles():
    label.config(text="Vous avez choisi l'option 1")

    ipAddr = None # Addresse IP d'un appareil connu (forcer la connaissance du réseau)
    object = None
    ipAddr = yc.getAvailableObjects()

def choix2connecterIP():
    label.config(text="Vous avez choisi l'option 2")

    ipAddr = None # Addresse IP d'un appareil connu (forcer la connaissance du réseau)
    object = None
    if ipAddr == None:
        print("Pas d'addresse IP configurée. Connexion impossible.\n")
    else:
        object = yc.connectObject(ipAddr)

def choix3allumerLampe():
    label.config(text="Vous avez choisi l'option 3")

    ipAddr = None # Addresse IP d'un appareil connu (forcer la connaissance du réseau)
    object = None
    if object == None:
        print("Pas d'objet connecté. Relancer et se connecter à un appareil.\n")
    else:
        if ipAddr == None:
            print("Pas d'objet connecté. Sélectionner une addresse IP, se connecter, et retenter.\n")
        else:
            yc.turnBulb(object,1)

def choix4eteindreLampe():
    label.config(text="Vous avez choisi l'option 4")
    ipAddr = None # Addresse IP d'un appareil connu (forcer la connaissance du réseau)
    object = None
    if object == None:
        print("Pas d'objet connecté. Relancer et se connecter à un appareil.\n")
    else:
        if ipAddr == '0':
            print("Pas d'objet connecté. Sélectionner une addresse IP, se connecter, et retenter.\n")
        else:
            yc.turnBulb(object,0)

def choix5lancerDemo():
    label.config(text="Vous avez choisi l'option 5")
    ipAddr = None # Addresse IP d'un appareil connu (forcer la connaissance du réseau)
    object = None

    # Script démo
    ipAddr = yc.getAvailableObjects()
    object = yc.connectObject(ipAddr)
    yc.turnBulb(object,1) # Allumer
    # yc.turnBulb(object,0) # Éteindre

def execChoiceFunc(choix):
    ipAddr = None # Addresse IP d'un appareil connu (forcer la connaissance du réseau)
    object = None
    
    # Choix 1 : Monter les adresses ip disponibles
    if (choix) == montrerIPdispo : 
        choix1ipDisponibles()
    
    # Choix 2 : Se connecter à une adresse ip
    elif (choix) == connexionIPchoisie :
        choix2connecterIP() 
        
        
    # Choix 3 : Allumer la lampe 
    elif (choix) == allumerLampe : 
        choix3allumerLampe()

    # Choix 4 : Eteindre l'appareil 
    elif (choix) == eteindreLampe : 
        choix4eteindreLampe()

    # Choix 5 : Lancer la démonstration
    elif int(choix) == 5:
        choix5lancerDemo()

    # Si rien n'est disponible
    else: 
        print("choix invalide, retenter.\n")

    
def affichageImage1(fenetre):

    espacement = 26.66
    tailleImg = 256

    # Charger une image1 et redimensionner
    image1 = PhotoImage(file="imgs/RechercheIp.png")  
    image1 = image1.subsample(4, 4)  # Facteur de sous-échantillonnage (ajuster selon vos besoins)

    # Charger une image2 et redimensionner
    image2 = PhotoImage(file="imgs/ConnexionToBulb.png")  
    image2 = image2.subsample(4, 4)  # Facteur de sous-échantillonnage (ajuster selon vos besoins)

    # Charger une image3 et redimensionner
    image3 = PhotoImage(file="imgs/BulbOn.png")  
    image3 = image3.subsample(4, 4)  # Facteur de sous-échantillonnage (ajuster selon vos besoins)

    # Charger une image4 et redimensionner
    image4 = PhotoImage(file="imgs/BulbOff.png")  
    image4 = image4.subsample(4, 4)  # Facteur de sous-échantillonnage (ajuster selon vos besoins)

    # Charger une image5 et redimensionner
    image5 = PhotoImage(file="imgs/Demo.png")  
    image5 = image5.subsample(4, 4)  # Facteur de sous-échantillonnage (ajuster selon vos besoins)

    fenetre.image1 = image1
    canvas = tk.Canvas(fenetre, width=image1.width(), height=image1.height())
    canvas.place(x=espacement, y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image1)

    fenetre.image2 = image2
    canvas = tk.Canvas(fenetre, width=image2.width(), height=image2.height())
    canvas.place(x=2 * espacement + tailleImg, y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image2)

    fenetre.image3 = image3
    canvas = tk.Canvas(fenetre, width=image3.width(), height=image3.height())
    canvas.place(x=3 * espacement + 2 * tailleImg, y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image3)

    fenetre.image4 = image4
    canvas = tk.Canvas(fenetre, width=image4.width(), height=image4.height())
    canvas.place(x=4 * espacement + 3 * tailleImg , y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image4)

    fenetre.image5 = image5
    canvas = tk.Canvas(fenetre, width=image5.width(), height=image5.height())
    canvas.place(x=5 * espacement + 4 * tailleImg, y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image5)

    bouton1 = tk.Button(fenetre, text="Available IP", command=choix1ipDisponibles)
    x_bouton1 = espacement + (tailleImg - bouton1.winfo_reqwidth() )/ 2
    bouton1.place(x=x_bouton1, y=150 + image1.height() + 10)  # Ajuster la position verticale en ajoutant 10 pixels

    bouton2 = tk.Button(fenetre, text="Connect IP", command=choix2connecterIP)
    x_bouton2 = 2 * espacement + tailleImg + (tailleImg - bouton2.winfo_reqwidth() )/ 2
    bouton2.place(x=x_bouton2, y=150 + image2.height() + 10)  # Ajuster la position verticale en ajoutant 10 pixels

    bouton3 = tk.Button(fenetre, text="Turn on", command=choix3allumerLampe)
    x_bouton3 = 3 * espacement + 2 * tailleImg + (tailleImg - bouton3.winfo_reqwidth() )/ 2
    bouton3.place(x=x_bouton3, y=150 + image3.height() + 10)  # Ajuster la position verticale en ajoutant 10 pixels

    bouton4 = tk.Button(fenetre, text="Turn off", command=choix4eteindreLampe)
    x_bouton4 = 4 * espacement + 3 * tailleImg + (tailleImg - bouton4.winfo_reqwidth() )/ 2
    bouton4.place(x=x_bouton4, y=150 + image4.height() + 10)  # Ajuster la position verticale en ajoutant 10 pixels

    bouton5 = tk.Button(fenetre, text="Demo", command=choix5lancerDemo)
    x_bouton5 = 5 * espacement + 4 * tailleImg + (tailleImg - bouton5.winfo_reqwidth() )/ 2
    bouton5.place(x=x_bouton5, y=150 + image5.height() + 10)  # Ajuster la position verticale en ajoutant 10 pixels

def creer_fenetre():
    fenetre = tk.Tk()
    fenetre.title("Application Graphique")

    fenetre.attributes('-fullscreen', True)

    label = tk.Label(fenetre, text="Cliquez sur une option")
    label.pack()

    affichageImage1(fenetre)

    bouton_quitter = tk.Button(fenetre, text="Quitter l'application", command=fenetre.destroy)
    bouton_quitter.pack()

    return fenetre, label



def lancer_interface():
    fenetre.mainloop()

# Programme principal
fenetre, label = creer_fenetre()
lancer_interface()






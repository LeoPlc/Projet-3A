from yeelight import discover_bulbs, Bulb
import readline

import yeelight_connexion as yc

import tkinter as tk


# Lampe Xiaomi Mathis
# 192.168.1.58

# Constants definition
montrerIPdispo = 1
connexionIPchoisie = 2
allumerLampe = 3
eteindreLampe = 4
lancerDemo = 5


def choixFunction():
    print("Options disponibles :\n'1': addresses IP disponibles\n'2': se connecter à une addresse IP\n'3':Allumer l'appareil.\n'4':Eteindre l'appareil connecté.\n'5': lancer la démo\n")
    choix = input("Choisissez une option: \n")    
    print("votre choix:", choix)
    return choix

def choix1ipDisponibles():
    label.config(text="Vous avez choisi l'option 1")

    ipAddr = None # Addresse IP d'un appareil connu (forcer la connaissance du réseau)
    object = None
    ipAddr = yc.getIpAddr()

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
        if ipAddr == '0':
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
    ipAddr = yc.getIpAddr()
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

    

def creer_fenetre():
    fenetre = tk.Tk()
    fenetre.title("Application Graphique")

    fenetre.attributes('-fullscreen', True)

    label = tk.Label(fenetre, text="Cliquez sur une option")
    label.pack()

    bouton1 = tk.Button(fenetre, text="Option 1", command=choix1ipDisponibles)
    bouton1.pack()

    bouton2 = tk.Button(fenetre, text="Option 2", command=choix2connecterIP)
    bouton2.pack()

    bouton3 = tk.Button(fenetre, text="Option 3", command=choix3allumerLampe)
    bouton3.pack()

    bouton4 = tk.Button(fenetre, text="Option 4", command=choix4eteindreLampe)
    bouton4.pack()

    bouton5 = tk.Button(fenetre, text="Option 5", command=choix5lancerDemo)
    bouton5.pack()


    bouton_quitter = tk.Button(fenetre, text="Quitter l'application", command=fenetre.destroy)
    bouton_quitter.pack()

    return fenetre, label



def lancer_interface():
    fenetre.mainloop()

# Programme principal
fenetre, label = creer_fenetre()
lancer_interface()


'''
Script d'exécution de l'application en terminal de commande:
    - Exécuter le main
    - Le main fait en sorte de tourner continuellement (ex - fonction run())
'''

#choix = choixFunction()   
#choix = int(choix)


#execChoiceFunc(choix)

    




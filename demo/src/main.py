from yeelight import discover_bulbs, Bulb
import readline

import yeelight_connexion as yc

# Lampe Xiaomi Mathis
# 192.168.1.58


'''

Script d'exécution de l'application en terminal de commande:
    - Exécuter le main
    - Le main fait en sorte de tourner continuellement (ex - fonction run())
    
'''



def run():

    choix = input("Choisissez une option: \n")
        
    ipAddr = '192.168.1.58' # Addresse IP d'un appareil connu (forcer la connaissance du réseau)
    object = None

    if choix == 1:
        ipAddr = yc.getIpAddr()
    elif choix == 2:
        if ipAddr == '0':
            print("Pas d'addresse IP configurée. Connexion impossible.\n")
        else: 
            object = yc.connectObject(ipAddr)
    elif choix == 3:
        if object == None:
            print("Pas d'objet connecté. Relancer et se connecter à un appareil.\n")
        else:
            if ipAddr == '0':
                print("Pas d'objet connecté. Sélectionner une addresse IP, se connecter, et retenter.\n")
            else:
                yc.turnBulb(object,1)
    elif object == 4:
        if object == None:
            print("Pas d'objet connecté. Relancer et se connecter à un appareil.\n")
        else:
            if ipAddr == '0':
                print("Pas d'objet connecté. Sélectionner une addresse IP, se connecter, et retenter.\n")
            else:
                yc.turnBulb(object,0)
            
            
    


print("Options disponibles :\n'1': addresses IP disponibles\n'2': se connecter à une addresse IP\n'3':Allumer l'appareil.\n'4':Eteindre l'appareil connecté")
run()
import paho.mqtt.client as mqtt
import time

class Model:
    
    def __init__(self):
        self.value = ''
        
    #Lancer la recherche des IoT disponibles
    
    def _get_available_IoT(self):
        
        print("get_available_iot_pushed")
        
        return ['IoT 1','IoT 2','IoT 3','IoT 4']
        
    
    #Gestion des fonctionnalités : Functions management
    
    def main(self):
        pass

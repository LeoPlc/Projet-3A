from view import View 
from model import Model

class Controller: 
    def __init__(self):
        self.view = View(self)
        self.model = Model(self.view)
        
    def main(self):
        self.view.main()
    
    # Fonction d'envoi d'une commande MQTT
    def send_mqtt_msg(self):
        # Affichage de la roue des couleurs RGB, sélection et récupération de la couleur et transmission vers l'objet de cette dernière afin que ce dernier puisse la transmettre
        rawColor = self.view.chose_color()
        self.model._bulb.set_properties(rawColor)

    def update_brightness(self, value):
        # Mise à jour de la luminosité en fonction du choix utilisateur
        self.model._bulb.update_brightness(value)

    # Fonction actuellement non fonctionnelle (du moins dans les tests effectués), normalement permettant d'afficher température / humidité de la part de notre capteur Zigbee de la marque Tuya
    def update_sensor_data(self):
        sensor_data = self.model.update_sensor_data()
        self.view.display_sensor_data(sensor_data)
    
if __name__ == '__main__':
    zigbeeApp = Controller()
    zigbeeApp.main()

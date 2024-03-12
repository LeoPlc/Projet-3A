import paho.mqtt.client as mqtt
from tkinter import colorchooser
import json 
from rgbxy import Converter

# Classe permettant de décrire ce qui est commun à tous les appareils Zigbee
class ZigbeeToMQTT:
    def __init__(self):
        self._client = mqtt.Client()
        
        # port de connexion et addresse
        self._brokerAddr = "localhost"
        self._brokerPort = 1883
        
    # Fonction d'envoi de commandes MQTT
    def send_message(self, message, topic):
        # Connexion au client mqtt (donc à l'appareil zigbee visé)
        self._client.connect(self._brokerAddr, self._brokerPort, 60)
        # Conversion du message à envoyer
        message_json = json.dumps(message)
        # Transmission du message
        self._client.publish(topic, message_json)


# Classe spécifique aux capteurs Zigbee, héritant d'une classe ZigbeeToMQTT contenant des méthodes communes à tous les IoT zigbee...

class Sensor(ZigbeeToMQTT):
    
    def __init__(self):
        super().__init__()
        
        self._message = ''
        
        # Topic de notre capteur de température
        self._topic = "zigbee2mqtt/T_H_zigbeeSensor"
    
    
    def get_temperature(self):
        pass
    
    def get_humidity(self):
        pass
    
    
    # Fonction permettant de récupérer les données provenant du capteur Zigbee
    def subscribe_sensor(self):
        # Connexion au clien via une adresse (localhost, initialisée dans la classe parent) et un port (1883, initialisé dans classe parent aussi)
        self._client.connect(self._brokerAddr, self._brokerPort, 60)
        self._client.subscribe(self._topic)
        self._client.on_message = self.get_info
        self._client.loop_start()
    
    # Fonction de récupération et mise à jour des données brutes
    def get_info(self, client, userdata, message):
        payload = message.payload.decode("utf-8")
        data = json.loads(payload)
        self.update_sensor_data(data)

    # Fonction de mise à jour des données pour les afficher
    def update_sensor_data(self, data):
        return f"Temperature: {data['temperature']} °C, Humidity: {data['humidity']}%"


# Classe spécifique aux ampoules Zigbee, héritant d'une classe ZigbeeToMQTT contenant des méthodes communes à tous les IoT zigbee...

class Bulb(ZigbeeToMQTT):
    
    def __init__(self):
        super().__init__()
        self._message = ''
        # Topic particulier de notre ampoule zigbee. Vous pouvez le remplacer par votre topic si vous le connaissez.
        self._topic = 'zigbee2mqtt/IKEA_Bulb/set'
        
    def set_properties(self, rawColor):
        self.set_color(rawColor)
        # self.set_brightness()
        
        self.send_message(self._message, self._topic)
        
        
    # Conversion de la couleur de rgb (format fourni par la roue des couleurs de tkinter) au format xy, compris par l'ampoule Zigbee
    def set_color(self, rawColor):

        converter = Converter()
        r, g, b = [x / 255.0 for x in rawColor]
        x, y = converter.rgb_to_xy(r, g, b)
        
        self._message = {"color": {"x": x, "y": y}}
        
    # Mise à jour de la luminosité de l'ampoule
    def set_brightness(self, brightness):
        return {'brightness': brightness }
    
    @classmethod
    def update_brightness(cls, value):
        cls._brightness = int(value)
        return cls._brightness

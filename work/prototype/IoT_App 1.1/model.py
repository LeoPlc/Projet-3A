# model.py
import paho.mqtt.client as mqtt
from rgbxy import Converter
import json
import requests
from view import View

class Model:
    brightness = 100  # Luminosité initialisée à 100 pour éviter d'aveugler les gens

    def __init__(self,view):
        self.view = view
        self._value = ''
        self._broker_addr = "localhost"
        self._broker_port = 1883
        self._topic = 'zigbee2mqtt/IKEA_Bulb/set'
        self._client = mqtt.Client()

    def _get_available_IoT(self):
        return self._topic

    @staticmethod
    def convert_rgb_and_brightness_to_zigbee(rgb, brightness):
        r, g, b = [x / 255.0 for x in rgb]
        converter = Converter()
        x, y = converter.rgb_to_xy(r, g, b)
        return {"color": {"x": x, "y": y}, "brightness": brightness}        

    def send_color_command(self):
        # Établir la connexion MQTT
        self._client.connect(self._broker_addr, self._broker_port, 60)

        rgb_color = self.view.on_color_and_brightness_selected()
        if rgb_color:
            message_data = self.convert_rgb_and_brightness_to_zigbee(rgb_color,self._brightness)

        if message_data:
            message_json = json.dumps(message_data)
            # Publier le message sur le topic
            self._client.publish(self._topic, message_json)

            # Déconnexion du broker
            self._client.disconnect()

    @classmethod
    def update_brightness(cls, value):
        cls._brightness = int(value)
        return cls._brightness


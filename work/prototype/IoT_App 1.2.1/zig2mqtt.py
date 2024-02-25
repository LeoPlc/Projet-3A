import paho.mqtt.client as mqtt
from tkinter import colorchooser
import json 
from rgbxy import Converter

class ZigbeeToMQTT:
    def __init__(self):
        self._client = mqtt.Client()
        
        self._brokerAddr = "localhost"
        self._brokerPort = 1883
        
    def send_message(self,message,topic):
        self._client.connect(self._brokerAddr, self._brokerPort, 60)
        message_json = json.dumps(message)
        self._client.publish(topic,message_json)


class Sensor(ZigbeeToMQTT):
    
    def __init__(self):
        super().__init__()
        
        self._message = ''
        self._topic = "zigbee2mqtt/0xec1bbdfffe0fb268"
    
    def get_temperature(self):
        pass
    
    def get_humidity(self):
        pass
    
    def subscribe_sensor(self):
        self._client.connect(self._brokerAddr,self._brokerPort,60)
        self._client.subscribe(self._topic)
        self._client.on_message = self.get_info
        self._client.loop_start()
    
    def get_info(self,client,userdata,message):
        payload = message.payload.decode("utf-8")
        data = json.loads(payload)
        self.update_sensor_data(data)

    def update_sensor_data(self, data):
        return f"Temperature: {data['temperature']} °C, Humidity: {data['humidity']}%"




class Bulb(ZigbeeToMQTT):
    
    def __init__(self):
        super().__init__()
        self._message = ''
        self._topic = 'zigbee2mqtt/IKEA_Bulb/set'
        
    def set_properties(self,rawColor):
        self.set_color(rawColor)
        # self.set_brightness()
        
        self.send_message(self._message,self._topic)
        
    def set_color(self,rawColor):

        converter = Converter()
        r,g,b = [x/255.0 for x in rawColor]
        x, y = converter.rgb_to_xy(r,g,b)
        
        self._message = {"color":{"x":x,"y":y}}
        
    def set_brightness(self,brightness):
        return {'brightness': brightness }
    
    @classmethod
    def update_brightness(self, value):
        self._brightness = int(value)
        return self._brightness
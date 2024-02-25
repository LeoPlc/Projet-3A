import paho.mqtt.client as mqtt
import json 

class ZigbeeToMQTT:
    def __init__(self):
        self._client = mqtt.Client()
        
        self._brokerAddr = "localhost"
        self._brokerPort = 1883
        
    def send_message(self,message,topic):
        self._client.connect(self._brokerAddr, self._brokerPort, 60)
        message_json = json.dumps(message)
        self._client.publish(topic,message_json)
        
    def get_status(self):
        print(self._client)
    
    
class Sensor(ZigbeeToMQTT):
    
    def __init__(self):
        super().__init__()
        

class Bulb(ZigbeeToMQTT):
    
    def __init__(self):
        super().__init__()
        self._message = ''
        self._topic = ''
        
    def _make_message(self,rawColor):
        pass
        
    def send_rgb_brightness(self):
        self.send_message(message,topic)
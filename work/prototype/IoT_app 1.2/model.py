
from zig2mqtt import ZigbeeToMQTT
from rgbxy import Converter

class Model:
    
    def __init__(self,view):
        self._mqttIoT = ZigbeeToMQTT()
        self.view = view
        
    def set_mqtt_color(self,brightness,topic):
        rawColor = self.view.on_color_and_brightness_selected()
        
        r, g, b = [x / 255.0 for x in rawColor]
        converter = Converter()
        x, y = converter.rgb_to_xy(r, g, b)
        
        message = {"color": {"x": x, "y": y}, "brightness": brightness}
        
        self._mqttIoT.send_message(message,topic)
        
    @classmethod
    def update_brightness(cls, value):
        cls._brightness = int(value)
        return cls._brightness
        
    def main(self):
        self.set_mqtt_color(self._brightness,"zigbee2mqtt/IKEA_Bulb/set")
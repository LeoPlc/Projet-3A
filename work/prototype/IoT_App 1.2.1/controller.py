from view import View 
from model import Model

class Controller: 
    def __init__(self):
        self.view = View(self)
        self.model = Model(self.view)
        
    def main(self):
        self.view.main()
    
    def send_mqtt_msg(self):
        rawColor = self.view.chose_color()
        self.model._bulb.set_properties(rawColor)

    def update_brightness(self,value):
        self.model._bulb.update_brightness(value)
        
    def update_sensor_info(self):
        return self.model._sensor.subscribe_sensor()
    
if __name__ == '__main__':
    zigbeeApp = Controller()
    zigbeeApp.main()
    
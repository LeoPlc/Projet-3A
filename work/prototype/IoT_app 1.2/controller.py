from view import View 
from model import Model

class Controller: 
    def __init__(self):
        self.view = View(self)
        self.model = Model(self.view)
        
    def main(self):
        self.view.main()
    
    def send_mqtt_msg(self):
        self.model.main()

    def update_brightness(self,value):
        self.model.update_brightness(value)
    
if __name__ == '__main__':
    zigbeeApp = Controller()
    zigbeeApp.main()
    
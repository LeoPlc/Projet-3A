# import zigpy


class ZigbeeDevice:
    
    def __init__(self):
        pass
    

    def connect(self):
        pass
    
    def getSensorValues(self):
        pass
    
    def sendCommand(self):
        pass
    
    
    
# Fonctionnalités communes à plusieurs appareils Zigbee
class ClusterZigbee:
    def __init__(self):
        pass
    
    def turnOn(self):
        pass
    
    def turnOff(self):
        pass
    
    


class RGB_Bulb(ZigbeeDevice, ClusterZigbee):
    def __init__(self):
        super().__init__()
from zig2mqtt import Bulb, Sensor


class Model:
    
    def __init__(self, view):
        self.view = view
        self._bulb = Bulb()
        self._sensor = Sensor()

    def update_sensor_data(self):
        return self._sensor.subscribe_sensor()

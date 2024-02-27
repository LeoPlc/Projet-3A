import tkinter as tk 
from tkinter import ttk
from tkinter import colorchooser

class View(tk.Tk):
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("zigbee2mqtt 1.2.1")

        color_button = tk.Button(self, text="Choisir une couleur", command=self.controller.send_mqtt_msg)
        color_button.pack(pady=20)

        brightness_scale = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL, label="brightness",
                                    command=self.controller.update_brightness)
        brightness_scale.pack(pady=10)
        
        self.sensor_label = tk.Label(self, text="Sensor Data: ")
        self.sensor_label.pack(pady=10)

        update_sensor_button = tk.Button(self, text="Mettre à jour le capteur", command=self.controller.update_sensor_data)
        update_sensor_button.pack(pady=10)
        
    def main(self):
        self.mainloop()
        
    def chose_color(self):
        return colorchooser.askcolor()[0]
    
    def display_sensor_data(self, data):
        self.sensor_label.config(text=f"Sensor Data: {data}")

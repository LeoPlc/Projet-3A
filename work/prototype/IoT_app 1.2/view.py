import tkinter as tk 
from tkinter import ttk
from tkinter import colorchooser

class View(tk.Tk):
    
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        
        
    def on_color_and_brightness_selected(self):
        return colorchooser.askcolor()[0]
        
        
    def main(self):
        color_button = tk.Button(self, text="Choisir une couleur", command=self.controller.send_mqtt_msg)
        color_button.pack(pady=20)
                # Curseur de luminosité
        brightness_scale = tk.Scale(self, from_=0, to=255, orient=tk.HORIZONTAL, label="brightness",
                                    command=self.controller.update_brightness)
        brightness_scale.pack(pady=10)
        
        self.mainloop()
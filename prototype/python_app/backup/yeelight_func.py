import yeelight
import func 
import tkinter as tk
import tkinter.messagebox



def lookfor_available_bulbs(available_bulbs):
    available_bulbs = yeelight.discover_bulbs()
    # available_bulbs= "hello"
    if not available_bulbs:
        tkinter.messagebox.showinfo("ERROR","No available bulb")
    else: 
        bulbs_window = tk.Tk()
        bulbs_window.title("Available bulbs:")
        bulbs_window.geometry("200x300")
        
        
        
        bulbs_window.mainloop()
        


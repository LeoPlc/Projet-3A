from tkinter import *


# Fonction de récupération d'un texte inséré dans une case (récupération d'une adresse IP par exemple)
def get_value(user_value, user_values, ip_list):
    user_values.append(user_value.get())
    update_list(user_values, ip_list)

# Fonction de réinitialisation des adresses IP
def reset_IP_addresses(user_values, ip_list):
    user_values.clear()
    update_list(user_values, ip_list)


# Mettre à jour la listbox en fonction des adresses IP insérées
def update_list(user_values, ip_list):
    ip_list.delete(0, END)
    for address in user_values:
        ip_list.insert(END, address)

def make_window(window_title):
    iot_window = Tk()
    iot_window.title(window_title)
    iot_window.geometry("200x200")
    
    iot_window.mainloop()
    return iot_window

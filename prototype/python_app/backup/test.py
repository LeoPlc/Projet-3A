import tkinter as tk
from tkinter.messagebox import *

import func as fc
import yeelight_func as yf

main_window = tk.Tk()
main_window.title("Crash test window")
main_window.geometry("400x250")
    
user_values = []
bulbs_available = []

# ------------------------------------- SCINDER LA FENÊTRE PRINCIPALE EN PLUSIEURS BLOCS ------------------------------------- #

left_bloc = tk.Frame(main_window, borderwidth=2)
left_bloc.place(x=10, y=10, width=150, height=140)

right_bloc = tk.Frame(main_window, borderwidth=2)
right_bloc.place(x=240, y=10, width=150, height=140)

bottom_bloc = tk.Frame(main_window, borderwidth=2)
bottom_bloc.place(relx=0.5, rely=0.9, anchor="s", width=300, height=70)

# ---------------------------------------------- GESTION DES ENTRÉES UTILISATEUR ---------------------------------------------- #

user_value = tk.StringVar()
entry_label = tk.Label(left_bloc, text="Saisir une adresse IP :")
entry_label.pack()

entry = tk.Entry(left_bloc, textvariable=user_value, width=20)
entry.pack()

ip_list = tk.Listbox(right_bloc, height=5, width=30)
ip_list.pack(pady=10)

# ---------------------------------------------------- GESTION DES BOUTONS ---------------------------------------------------- #

valid_button = tk.Button(left_bloc, text="valider", command=lambda: fc.get_value(user_value, user_values, ip_list))
valid_button.pack()

reset_button = tk.Button(left_bloc, text="Réinitialiser Adresses", command=lambda: fc.reset_IP_addresses(user_values, ip_list))
reset_button.pack()

discover_button = tk.Button(left_bloc, text= "rechercher...",command = lambda:yf.lookfor_available_bulbs(bulbs_available))
discover_button.pack()

exit_button = tk.Button(bottom_bloc, text="exit", command=main_window.quit)
exit_button.pack()

# --------------------------------------------------- AFFICHAGE DE LA FENÊTRE -------------------------------------------------- #

main_window.mainloop()

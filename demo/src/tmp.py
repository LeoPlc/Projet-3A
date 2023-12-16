import tkinter as tk
from tkinter import PhotoImage

def creer_fenetre():
    fenetre = tk.Tk()
    fenetre.title("Application Graphique")

    # Configurer la fenêtre en plein écran
    fenetre.attributes('-fullscreen', True)

    label = tk.Label(fenetre, text="Entrez votre nom:")
    label.place(x=50, y=50)

    entry = tk.Entry(fenetre)
    entry.place(x=200, y=50)

    # Calculer les dimensions de la fenêtre
    largeur_fenetre = fenetre.winfo_screenwidth()
    hauteur_fenetre = fenetre.winfo_screenheight()

    # Charger une image et redimensionner
    image = PhotoImage(file="imgTmp.png")  
    image = image.subsample(4, 4)  # Facteur de sous-échantillonnage (ajuster selon vos besoins)

    espacement = 26.66
    tailleImg = 256

    fenetre.image = image
    canvas = tk.Canvas(fenetre, width=image.width(), height=image.height())
    canvas.place(x=espacement, y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    
    fenetre.image = image
    canvas = tk.Canvas(fenetre, width=image.width(), height=image.height())
    canvas.place(x=espacement + tailleImg + espacement/2, y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    
    fenetre.image = image
    canvas = tk.Canvas(fenetre, width=image.width(), height=image.height())
    canvas.place(x=2 * espacement + 2 * tailleImg + espacement/2, y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    
    fenetre.image = image
    canvas = tk.Canvas(fenetre, width=image.width(), height=image.height())
    canvas.place(x=3 * espacement + 3 * tailleImg + espacement/2, y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    
    fenetre.image = image
    canvas = tk.Canvas(fenetre, width=image.width(), height=image.height())
    canvas.place(x=4 * espacement + 4 * tailleImg + espacement/2, y=150)
    canvas.create_image(0, 0, anchor=tk.NW, image=image)

    bouton = tk.Button(fenetre, text="Cliquez ici", command=lambda: bouton_clic(entry))

    # Calculer la position horizontale pour centrer le bouton
    x_bouton = (largeur_fenetre - bouton.winfo_reqwidth()) // 2
    bouton.place(x=x_bouton, y=150 + image.height() + 10)  # Ajuster la position verticale en ajoutant 10 pixels

    return fenetre, label, entry

def bouton_clic(entry):
    label.config(text="Bonjour, " + entry.get())

def lancer_interface():
    fenetre.mainloop()

# Programme principal
fenetre, label, entry = creer_fenetre()
lancer_interface()

print(160/6)

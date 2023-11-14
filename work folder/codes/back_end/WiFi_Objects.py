# Classe de base WiFiDevice
class WiFiDevice:
    def __init__(self, ip_address, port):
        self.ip_address = ip_address
        self.port = port
        # Autres attributs et méthodes d'initialisation

    def connect(self):
        # Code pour se connecter à l'appareil WiFi
        print(f"Connecté à l'appareil WiFi à l'adresse {self.ip_address}:{self.port}")

# Classe RGB_Bulb_WiFi héritant de WiFiDevice
class RGB_Bulb_WiFi(WiFiDevice):
    def __init__(self, ip_address, port):
        # Appel au constructeur de la classe de base WiFiDevice
        super().__init__(ip_address, port)

    # Vous n'avez pas besoin de réimplémenter la méthode connect, car elle est héritée de WiFiDevice

    # Implémentez les méthodes spécifiques pour l'ampoule RGB WiFi
    def turn_on(self):
        # Code pour allumer l'ampoule RGB WiFi
        print("Ampoule allumée")

    def turn_off(self):
        # Code pour éteindre l'ampoule RGB WiFi
        print("Ampoule éteinte")

# Exemple d'utilisation
bulb = RGB_Bulb_WiFi("192.168.0.100", 8080)

# Connectez-vous à l'ampoule WiFi
bulb.connect()

# Allumez l'ampoule WiFi
bulb.turn_on()

# Éteignez l'ampoule WiFi
bulb.turn_off()

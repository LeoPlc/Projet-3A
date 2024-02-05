from model import Model
from view import View

class Controller:
    
    def __init__(self):
        self.model = Model()
        self.view = View(self) #Instancie automatiquement dans la view
        
    
    def main(self):
        self.view.main()
        
    def show_available_iot(self,caption):
        if caption == 'Show available IoT':
            # Rafraîchir la liste des IoT disponibles
            
            self.view.available_IoTs = self.model._get_available_IoT()
            self.view.update_list()

        elif caption == 'connect IoT':
            pass
        
        elif caption == 'delete list':
            self.view.delete_list()
            
    
if __name__ == "__main__":
    IoT_app = Controller()
    IoT_app.main()
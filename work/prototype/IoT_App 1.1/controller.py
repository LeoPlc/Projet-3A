# controller.py
from model import Model
from view import View


class Controller:

    def __init__(self):

        self.view = View(self)  # Instancie automatiquement dans la view$
        self.model = Model(self.view)

    def main(self):
        self.view.main()

    def show_available_iot(self, caption):
        if caption == 'Show available IoT':
            # Rafraîchir la liste des IoT disponibles
            self.view.available_IoTs = self.model._get_available_IoT()
            self.view.update_list()

        elif caption == 'connect IoT':
            pass

        elif caption == 'delete list':
            self.view.delete_list()

    def send_color_command(self):
        self.model.send_color_command()

    def update_brightness(self, value):
        self.model.update_brightness(value)


if __name__ == "__main__":
    IoT_app = Controller()
    IoT_app.main()

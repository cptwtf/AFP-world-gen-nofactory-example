from Interfaces.Animal import Animal


class Hoomin(Animal):

    def __init__(self):
        super().__init__("Hoomin")

    def do_animal_stuff(self):
        print("*has depression and is late on paying bills*")



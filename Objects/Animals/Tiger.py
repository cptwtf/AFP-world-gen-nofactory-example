from Interfaces.Animal import Animal


class Tiger(Animal):

    def __init__(self):
        super().__init__("Tiger")

    def do_animal_stuff(self):
        print("*stalking the jungle like a chad*")




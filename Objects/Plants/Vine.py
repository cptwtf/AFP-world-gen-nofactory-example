from Interfaces.Plant import Plant


class Vine(Plant):

    def __init__(self):
        super().__init__("Vine")

    def do_plant_stuff(self):
        print("*strives, struggles, strangles >)*")

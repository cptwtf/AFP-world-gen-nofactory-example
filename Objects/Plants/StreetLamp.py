from Interfaces.Plant import Plant


class StreetLamp(Plant):

    def __init__(self):
        super().__init__("StreetLamp")

    def do_plant_stuff(self):
        print("an elaborate insect trap that hides the stars")


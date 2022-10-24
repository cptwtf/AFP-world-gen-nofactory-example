from Interfaces.Ground import Ground


class Swamp(Ground):

    def __init__(self):
        super().__init__("Swamp")

    def do_ground_stuff(self):
        print("home of toads")


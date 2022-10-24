from Interfaces.Ground import Ground


class Concrete(Ground):

    def __init__(self):
        super().__init__("Concrete")

    def do_ground_stuff(self):
        print("*suffocates earth*")


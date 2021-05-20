

class Jumper:

    def __init__(self):
        self.parachute = ["  ___  ", " /___\ ", " \   / ", "  \ /  "]


    def print_jumper(self, strikes):
        if strikes < 4:
            for z in self.parachute:
                print(z)

            print("   0   \n  /|\  \n  / \  \n\n^^^^^^^")
        else:
            print("   X   \n  /|\  \n  / \  \n\n^^^^^^^")

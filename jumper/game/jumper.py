

class Jumper:

    def __init__(self):
        self.par1 = "  ___  "
        self.par2 = " /___\ "
        self.par3 = " \   / "
        self.par4 = "  \ /  "
        self.parachute = ["  ___  ", " /___\ ", " \   / ", "  \ /  "]


    def print_jumper(self, strikes):
        if strikes < 4:
            i = 0
            for i in range(0, strikes):
                self.parachute.pop(0)

            for z in self.parachute:
                print(z)

            print("   0   \n  /|\  \n  / \  \n\n^^^^^^^")
        else:
            print("   X   \n  /|\  \n  / \  \n\n^^^^^^^")

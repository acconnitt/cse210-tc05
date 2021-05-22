class Jumper:

    def __init__(self):
        # initilize the jumper class
        self.parachute = ["  ___  ", " /___\ ",  " \   / ",
                          "  \ /  "]  # Array that has parachute drawing

    def print_jumper(self, strikes):
        if strikes < 4:  # Check if strikes are < 4
            for z in self.parachute:  # Print a live guy
                print(z)
            print("   0   \n  /|\  \n  / \  \n\n^^^^^^^")
        else:
            # print dead guy if strikes are > 4
            print("   X   \n  /|\  \n  / \  \n\n^^^^^^^")

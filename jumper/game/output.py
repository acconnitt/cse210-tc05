


class Output:

    def print_jumper(self, strikes, jumper):
        jumper.print_jumper(strikes)

    def print_blanks(self, word):
        print(*word.blanks, sep=" ")

    def print_win(self):
        print("Congrats, you guessed the word!")

    def print_loss(self):
        print("Sorry, you hit the ground a little too hard!")

class Output:

    def print_jumper(self, strikes, jumper):
        jumper.print_jumper(strikes) # Print the jumper figure

    def print_blanks(self, word):
        print(*word.blanks, sep=" ")#Print blanks lines and space

    def print_win(self):
        print("Congrats, you guessed the word!")#Print when user guesses all letter correctly

    def print_loss(self):
        print("Sorry, you hit the ground a little too hard!")#Print when user lose after 4 tries
        

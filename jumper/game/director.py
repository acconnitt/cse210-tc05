from game.jumper import Jumper
from game.word import Word
from game.output import Output


class Director:

    # Method initializer for the Director class
    def __init__(self):
        """Attributesof of the class"""
        """Objects of the class"""
        self.strikes = 0  # Strikes start at 0
        self.jumper = Jumper()  # Call the Jumper Class
        self.word = Word()  # Call the Word Class
        self.output = Output()  # Call the Output Class
        self.keep_playing = True  # Keep playing while true
        self.guess = ""  # Empty string to hold user letter input

    def start_game(self):
        """Start the game and keep playing until game ends
           or user ends it"""

        while self.keep_playing:
            # Calls print_blanks method from Output Class
            self.output.print_blanks(self.word)
            # Calls print_jumper method from Jumper Class
            self.output.print_jumper(self.strikes, self.jumper)
            self.get_letter()  # Calls get_letter method
            # Get a strike if letter is not in the word
            if not self.word.check_letter(self.guess):
                # Abstraction: Pop removes an object from the list parachute and returns it
                self.jumper.parachute.pop(0)
                self.strikes += 1  # Add one to strike
                if self.strikes >= 4:  # Check if strikes reaches the maximum
                    self.output.print_blanks(self.word)
                    self.output.print_jumper(self.strikes, self.jumper)
                    self.output.print_loss()
                    self.keep_playing = False  # Change keep.playing to false = finished the game
            else:
                # If the guess letter matches a letter in the word
                self.word.replace_blank(self.guess) # Call replace_blank method from Word Class
                if self.word.check_blanks() == False:  # Call check_blanks funtion to see if it is true or false
                    self.output.print_blanks(self.word)
                    self.output.print_win()# Call print_win from Output Class
                    self.keep_playing = False # Change keep playing to false to end game

    def get_letter(self):
        self.guess = input("Guess a letter [a-z]: ")  # Get a letter from user

from game.jumper import Jumper
from game.word import Word
from game.output import Output

class Director:

    def __init__(self):
        self.strikes = 0
        self.jumper = Jumper()
        self.word = Word()
        self.output = Output()
        self.keep_playing = True
        self.guess = ""


    def start_game(self):
        while self.keep_playing:
            self.output.print_blanks(self.word)
            self.output.print_jumper(self.strikes, self.jumper)
            self.get_letter()
            if not self.word.check_letter(self.guess):
                self.jumper.parachute.pop(0)
                self.strikes += 1
                if self.strikes >= 4:
                    self.output.print_blanks(self.word)
                    self.output.print_jumper(self.strikes, self.jumper)
                    self.output.print_loss()
                    self.keep_playing = False
            else:
                self.word.replace_blank(self.guess)
                if self.word.check_blanks() == False:
                    self.output.print_blanks(self.word)
                    self.output.print_win()
                    self.keep_playing = False


    def get_letter(self):
        self.guess = input("Guess a letter [a-z]: ")

import random


class Word():

    def __init__(self):
        self.words = ["abruptly", "beekeeper", "blizzard", "cobweb", "flapjack", "haphazard", "jackpot", "syntax",
                      "abstraction", "microwave", "witchcraft", "zombie", "corruption", "jogging", "keyboard"]
        self.choice = random.randint(0, 14)
        self.the_word = self.words[self.choice]
        self.blanks = []
        self.make_blanks()

    def check_letter(self, letter):
        if letter in self.the_word:
            self.replace_blank(letter)
            return True
        else:
            return False

    def make_blanks(self):
        for _ in self.the_word:
            self.blanks.append("_")
        return self.blanks

    def replace_blank(self, letter):
        for i in range(0, len(self.the_word)):
            if letter == self.the_word[i]:
                self.blanks[i] = letter

    def check_blanks(self):
        if "_" in self.blanks:
            return True
        else:
            return False

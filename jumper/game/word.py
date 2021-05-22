import random

class Word():

    def __init__(self):
        # Array that holds words that will be used for the user to guess later on
        self.words = ["abruptly", "beekeeper", "blizzard", "cobweb", "flapjack", "haphazard", "jackpot", "syntax",
                      "abstraction", "microwave", "witchcraft", "zombie", "corruption", "jogging", "keyboard"]
        self.choice = random.randint(0, 14)  # gets a random number from 0-14
        # Choose a word based on number from self.choice
        self.the_word = self.words[self.choice]
        self.blanks = []  # Empty array to be filled in with "_"s
        self.make_blanks()  # Calls make_blanks method

    def check_letter(self, letter):
        if letter in self.the_word:  # Check if the user's letter guess is part of the word
            self.replace_blank(letter)  # Call the replace_blank method
            return True  # If letter is part of the word return true
        else:
            return False  # If letter is not part of the word return false

    def make_blanks(self):
        # Replace word letters with "_" based on words length
        for _ in self.the_word:
            # Array self.blanks is being filled in
            self.blanks.append("_")
        return self.blanks

    def replace_blank(self, letter):
        for i in range(0, len(self.the_word)):  # Start on 0 and ends on word length
            # Check if guess letter is equal to word index
            if letter == self.the_word[i]:
                # Change blank to letter in the correct index of the self.blanks array
                self.blanks[i] = letter

    def check_blanks(self):
        if "_" in self.blanks:  # Check if there are any more blanks in word and return
            return True  # If there are return true
        else:
            return False  # If there are not return false

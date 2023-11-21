
import random
class Game:
    def __init__(self, words):
        self.words = words
        self.word_to_guess = ""
        self.guesses_remaining = 7
        self.guesses = []
    
    def select_random_word(self):
        self.word_to_guess = random.choice(self.words)
    
    def display_word(self):
        display = ""
        for letter in self.word_to_guess:
            if letter in self.guesses:
                display += letter
            else:
                display += "_"
        return display
    
    def make_guess(self, letter):
        if letter in self.guesses:
            return "Вы уже догадались, что это за буква"
        self.guesses.append(letter)
        if letter not in self.word_to_guess:
            self.guesses_remaining -= 1
        if self.check_win():
            return "Поздравляю ты угадал" + self.word_to_guess
        elif self.check_loss():
            return "Ты проиграл словом было:" + self.word_to_guess
        return self.display_word()
    
    def check_win(self):
        return set(self.word_to_guess).issubset(self.guesses)
    
    def check_loss(self):
        return self.guesses_remaining == 0
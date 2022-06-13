import string

from core.wordle_game.run import run_wordle_game


class GamePlayer:
    def __init__(self):
        self.game = run_wordle_game()
        self.all_previous_results = {}
        self.letter_dictionary = {
            letter: {"present": None, "position": None, "available_positions": [0, 1, 2, 3, 4]}
            for letter in string.ascii_lowercase
        }

    def check_word(self, word: str):
        word_results = self.game.check_word(word)
        self.all_previous_results = self.game.all_combined_results
        self.update_letter_dictionary(word_results)
        if self.game.check_victory():
            return "You are the best!"
        else:
            return self.letter_dictionary

    def update_letter_dictionary(self, word_results):
        for letter in word_results:
            word_results[letter]["present"] = self.letter_dictionary[letter]["present"]
            for position, check in word_results[letter]["check_positions"]:
                if check:
                    self.letter_dictionary[letter]["position"] = position
                    self.letter_dictionary[letter]["available_positions"] = position
                else:
                    self.letter_dictionary[letter]["available_positions"].pop(position)

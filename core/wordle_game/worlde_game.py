from typing import Any, Dict, List

from core.wordle_game.check_char_positions import check_char_positions


class WordleGame:
    def __init__(self, answer: str, attempts_limit: int = 6):
        self.all_combined_results: Dict[str, Dict[str, Any]] = {}
        self.attempt_index: int = 0
        self.found_letters = {number: None for number in range(len(answer))}
        self._answer = answer
        self.guesses: List[str] = []
        self.attempts_limit = attempts_limit

    def check_word(self, input_word: str):
        self.attempt_index += 1
        self._check_attempts_limit()
        # TODO: check if word is in all_words.json
        word_check_results = check_char_positions(input_word, self._answer)
        self._update_results(word_check_results)
        # victory = self.check_victory() #TODO: when class created add this to one of its fields
        self.guesses.append(input_word)
        return word_check_results

    def _update_results(self, word_check_results: Dict[str, Dict[str, Any]]):
        for letter, letter_result in word_check_results.items():
            if letter not in self.all_combined_results:
                self.all_combined_results[letter] = {"present": None, "checked_positions": {}}
                self.all_combined_results[letter]["present"] = letter_result["present"]
                self.all_combined_results[letter]["checked_positions"] = letter_result["checked_positions"]
            else:
                self.all_combined_results[letter]["checked_positions"].update(letter_result["checked_positions"])

            for index, valid_position in letter_result["checked_positions"].items():
                if valid_position:
                    self.found_letters[index] = letter

    def _check_attempts_limit(self):
        if self.attempt_index > self.attempts_limit:
            raise Exception(f"Attempt limit is {self.attempts_limit}, is passed!") #TODO: test for this

    def check_victory(self) -> bool:
        if list(self._answer) == self.found_letters.values():
            print(f"Victory! The answer is {self._answer}!")  #TODO: test for this
            return True
        return False

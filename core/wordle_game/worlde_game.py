from typing import List, Dict, Union


class WordleGame:
    def __init__(self, answer):
        self.all_combined_results: Dict[str: Dict[str: Union[str, bool]]] = None
        self.attempt_index: int = 0
        self.answer = answer
        self.guesses: List[str]

    def update_results(self, word_check_results):
        ... #all combined results + check_chars(slowa) sprawdzac czy w combined results jest klucz

    # jesli jest to if position =
    # jesli nie ma k

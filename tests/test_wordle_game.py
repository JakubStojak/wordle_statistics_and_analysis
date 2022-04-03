from unittest import TestCase
from core.wordle_game.worlde_game import WordleGame
from core.wordle_algorithm.check_char_positions import check_char_positions


class TestWordleGame(TestCase):
    def test_update_guesses(self):
        answer = "wared"
        wordle_game = WordleGame(answer)
        results = check_char_positions("water", answer)
        wordle_game.update_results(results)
        expected = ...
        self.assertEqual(expected, wordle_game.all_combined_results)


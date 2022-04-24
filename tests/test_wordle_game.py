from unittest import TestCase
from core.wordle_game.worlde_game import WordleGame


class TestWordleGame(TestCase):
    def test_check_word(self):
        answer = "wared"
        wordle_game = WordleGame(answer)
        wordle_game.check_word("water")
        expected = {
            "w": {'present': True, "checked_positions": {0: True}},
            "a": {'present': True, "checked_positions": {1: True}},
            "t": {'present': False, "checked_positions": {2: False}},
            "e": {'present': True, "checked_positions": {3: True}},
            "r": {'present': True, "checked_positions": {4: False}}
        }
        self.assertEqual(expected, wordle_game.all_combined_results)

    def test_game_multiple_stages(self):
        answer = "wared"
        wordle_game = WordleGame(answer)
        wordle_game.check_word("beats")
        wordle_game.check_word("marne")
        expected = {
            "b": {'present': False, 'checked_positions': {0: False}},
            "e": {'present': True, 'checked_positions': {1: False, 4: False}},
            "a": {'present': True, 'checked_positions': {1: True, 2: False}},
            "t": {'present': False, 'checked_positions': {3: False}},
            "s": {'present': False, 'checked_positions': {4: False}},
            "m": {'present': False, 'checked_positions': {0: False}},
            "r": {'present': True, 'checked_positions': {2: True}},
            "n": {'present': False, 'checked_positions': {3: False}}
        }
        self.assertEqual(expected, wordle_game.all_combined_results)

    def test_check_repeated_items(self):
        answer = "olive"
        wordle_game = WordleGame(answer)
        wordle_game.check_word("water")
        wordle_game.check_word("copes")
        wordle_game.check_word("heros")
        wordle_game.check_word("guild")
        wordle_game.check_word("veils")
        wordle_game.check_word("olive")
        expected = {
            "w": {'present': False, "checked_positions": {0: False}},
            "a": {'present': False, "checked_positions": {1: False}},
            "t": {'present': False, "checked_positions": {2: False}},
            "e": {'present': True, "checked_positions": {3: False, 1: False, 4: True}},
            "r": {'present': False, "checked_positions": {4: False, 2: False}},
            "c": {'present': False, "checked_positions": {0: False}},
            "o": {'present': True, "checked_positions": {1: False, 3: False, 0: True}},
            "p": {'present': False, "checked_positions": {2: False}},
            "s": {'present': False, "checked_positions": {4: False}},
            "h": {'present': False, "checked_positions": {0: False}},
            "g": {'present': False, "checked_positions": {0: False}},
            "u": {'present': False, "checked_positions": {1: False}},
            "i": {'present': True, "checked_positions": {2: True}},
            "l": {'present': True, "checked_positions": {3: False, 1: True}},
            "d": {'present': False, "checked_positions": {4: False}},
            "v": {'present': True, "checked_positions": {0: False, 3: True}}
        }
        self.assertEqual(expected, wordle_game.all_combined_results)

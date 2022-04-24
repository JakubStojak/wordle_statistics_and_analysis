from unittest import TestCase
from core.wordle_game.check_char_positions import check_char_positions


class TestCheckChars(TestCase):
    def test_check_chars(self):
        input_word = "water"
        answer = "wared"
        expected = {
            "w": {'present': True, "checked_positions": {0: True}},
            "a": {'present': True, "checked_positions": {1: True}},
            "t": {'present': False, "checked_positions": {2: False}},
            "e": {'present': True, "checked_positions": {3: True}},
            "r": {'present': True, "checked_positions": {4: False}}
        }
        self.assertEqual(expected, check_char_positions(input_word, answer))

    def test_letter_error(self):
        input_word = "twoo"
        answer = "pao"
        with self.assertRaises(ValueError) as error:
            check_char_positions(input_word, answer)
            assert error.exception == "Not enough letters!"

    def test_not_alpha_error(self):
        input_word = "26934"
        answer = "*$28d"
        with self.assertRaises(ValueError) as error:
            check_char_positions(input_word, answer)
            assert error.exception == "Invalid characters in input"

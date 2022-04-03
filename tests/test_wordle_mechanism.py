from unittest import TestCase
from core.wordle_algorithm.check_char_positions import check_char_positions


class TestCheckChars(TestCase):
    def test_check_chars(self):
        input_word = "water"
        answer = "wared"
        expected = {"w": {'present': True, 'position': 0, "valid_position": True},
                    "a": {'present': True, 'position': 1, "valid_position": True},
                    "t": {'present': False, 'position': 2, "valid_position": False},
                    "e": {'present': True, 'position': 3, "valid_position": True},
                    "r": {'present': True, 'position': 4, "valid_position": False}}
        self.assertEqual(expected, check_char_positions(input_word, answer))

### TESTY NA ERROR

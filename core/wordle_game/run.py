import json
import random

from worlde_game import WordleGame

with open("core/word_sets/all_possible_answers.json", "r") as file:
    all_answers = json.load(file)


def run_wordle_game() -> WordleGame:
    answer = random.choice(all_answers)
    game = WordleGame(answer, attempts_limit=6)
    return game

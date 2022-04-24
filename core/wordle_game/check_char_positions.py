def check_char_positions(input_word: str, answer: str):
    letter_positions_info = {}
    if len(input_word) != 5 or len(answer) != 5:
        raise ValueError("Not enough letters!")
    if not input_word.isalpha():
        raise ValueError("Invalid characters in input")
    input_word_split = list(input_word)
    for index, letter in enumerate(input_word_split):
        letter_position_in_answer = answer.find(letter)
        if letter_position_in_answer == -1:
            letter_positions_info[letter] = {'present': False, "checked_positions": {index: False}}
        elif letter_position_in_answer == index:
            letter_positions_info[letter] = {'present': True, "checked_positions": {index: True}}
        else:
            letter_positions_info[letter] = {'present': True, "checked_positions": {index: False}}
    return letter_positions_info

import split


def wordle_algorithm(input_word: str, answer: str):
    if len(input_word) != 5 or len(answer) != 5:
        raise ValueError("Not enough letters!")
    default_dictionary = {"a": None, "a_position": None, "b": None, "b_position": None,
                          "c": None, "c_position": None, "d": None, "d_position": None,
                          "e": None, "e_position": None, "f": None, "f_position": None,
                          "g": None, "g_position": None, "h": None, "h_position": None,
                          "i": None, "i_position": None, "j": None, "j_position": None,
                          "k": None, "k_position": None, "l": None, "l_position": None,
                          "m": None, "m_position": None, "n": None, "n_position": None,
                          "o": None, "o_position": None, "p": None, "p_position": None,
                          "q": None, "q_position": None, "r": None, "r_position": None,
                          "s": None, "s_position": None, "t": None, "t_position": None,
                          "u": None, "u_position": None, "v": None, "v_position": None,
                          "w": None, "w_position": None, "x": None, "x_position": None,
                          "y": None, "y_position": None, "z": None, "z_position": None}
    input_word_split = split.split(input_word)
    answer_split = split.split(answer)
    for letter in input_word_split:
        if letter in answer_split:
            default_dictionary[letter] = True
            if input_word_split.index(letter) == answer_split.index(letter):
                default_dictionary["%s_position" % letter] = input_word_split.index(letter) + 1
            else:
                default_dictionary["%s_position" % letter] = "not %s" % (input_word_split.index(letter) + 1)

        else:
            default_dictionary[letter] = False
    print(default_dictionary)


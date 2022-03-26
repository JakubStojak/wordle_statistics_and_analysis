from unittest import TestCase

from wordle_algorithm.wordle_algorithm import wordle_algorithm


class TestAlgorithm(TestCase):
    def test_algorithm(self):
        algorithm_result = wordle_algorithm("water", "wared")
        expected_result = {"a": True, "a_position": 2, "b": None, "b_position": None,
                           "c": None, "c_position": None, "d": None, "d_position": None,
                           "e": True, "e_position": 4, "f": None, "f_position": None,
                           "g": None, "g_position": None, "h": None, "h_position": None,
                           "i": None, "i_position": None, "j": None, "j_position": None,
                           "k": None, "k_position": None, "l": None, "l_position": None,
                           "m": None, "m_position": None, "n": None, "n_position": None,
                           "o": None, "o_position": None, "p": None, "p_position": None,
                           "q": None, "q_position": None, "r": True, "r_position": "not 3",
                           "s": None, "s_position": None, "t": False, "t_position": None,
                           "u": None, "u_position": None, "v": None, "v_position": None,
                           "w": True, "w_position": 1, "x": None, "x_position": None,
                           "y": None, "y_position": None, "z": None, "z_position": None}
        self.assertEqual(algorithm_result, expected_result)

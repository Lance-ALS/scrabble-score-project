import unittest
from unittest.mock import patch
import time
from scrabble_game import ScrabbleGame

class TestScrabbleGame(unittest.TestCase):

    def setUp(self):
        self.game = ScrabbleGame()

    def test_calculate_score(self):
        self.assertEqual(self.game.calculate_score("cabbage"), 14)
      

    def test_case_insensitivity(self):
        self.assertEqual(self.game.calculate_score("DOG"), 5)
        self.assertEqual(self.game.calculate_score("dog"), 5)

    def test_invalid_word_input(self):
        with self.assertRaises(ValueError):
            self.game.validate_word("12345")  
        with self.assertRaises(ValueError):
            self.game.validate_word("hello!")

    def test_word_length_check(self):
        self.assertTrue(self.game.check_word_length("hello", 5))
        self.assertFalse(self.game.check_word_length("hello", 4))

    def test_random_word_length(self):
        word_length = self.game.generate_random_word_length()
        self.assertTrue(2 <= word_length <= 9)

    @patch('builtins.input', return_value='banana')
    def test_time_limit(self, mock_input):
        start_time = time.time()
        while time.time() - start_time < 16:
            pass
        self.assertEqual(self.game.play_round(), 0)

    def test_word_in_dictionary(self):
        self.assertTrue(self.game.validate_word("dog"))
        self.assertFalse(self.game.validate_word("notaword")) 

    @patch('builtins.input', return_value='quit')
    def test_quit_functionality(self, mock_input):
        self.assertEqual(self.game.play_round(), 'quit')

    def test_game_over(self):
        self.game.total_score = 50
        self.assertEqual(self.game.check_game_over(10), 50)

    def test_score_adjustment_with_time(self):
        score = self.game.adjust_score_based_on_time(10, 4)  
        self.assertEqual(score, 15)

        score = self.game.adjust_score_based_on_time(10, 6)  
        self.assertEqual(score, 13)

        score = self.game.adjust_score_based_on_time(10, 12)  
        self.assertEqual(score, 10)

if __name__ == '__main__':
    unittest.main()
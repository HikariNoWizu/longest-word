# tests/test_game.py
import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_game_is_valid(self):
        new_game = Game()
        new_game.grid = ["O", "Q", "U", "W", "R", "B", "A", "Z", "E"]
        word = "BAROQUE"
        #self.assertIsInstance(grid, Bool)
        self.assertTrue(new_game.is_valid(word))
        self.assertEqual(new_game.grid, ["O", "Q", "U", "W", "R", "B", "A", "Z", "E"])

    def test_game_is_invalid(self):
        new_game = Game()
        new_game.grid = ["O", "Q", "U", "W", "R", "B", "A", "Z", "E"]
        word = "BLABLA"
        self.assertFalse(new_game.is_valid(word))
        self.assertEqual(new_game.grid, ["O", "Q", "U", "W", "R", "B", "A", "Z", "E"])

    # tests/test_game.py
    # [...]
    def test_unknown_word_is_invalid(self):
        new_game = Game()
        new_game.grid = list('KWIENFUQW') # Force the grid to a test case:
        self.assertIs(new_game.is_valid('FEUN'), False)




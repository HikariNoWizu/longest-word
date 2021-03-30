"""module docstring"""
import random
import string
import requests

class Game:
    """class docstring"""

    def __init__(self):
        """Init docstring"""
        self.grid = [random.choice(string.ascii_uppercase) for i in range(9)]

    def is_valid(self, word):
        """Method docstring"""
        my_word_is_valid = True
        grid_copy = self.grid.copy()
        for letter in word:
            my_word_is_valid &= letter in grid_copy
            if my_word_is_valid:
                grid_copy.remove(letter)
        my_word_is_valid &= requests.get('https://wagon-dictionary.herokuapp.com/'+word).json()['found']
        return my_word_is_valid

    def extra_useless_method(self):
        """Method docstring"""
        # pylint: disable=missing-docstring
        # pylint: disable=too-few-public-methods

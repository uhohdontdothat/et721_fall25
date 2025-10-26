"""
Henry Perez
10/26/2025
Connect 4 Unit Tests
"""
from main import Connect4
import unittest

# Unit tests for switch_player(self)
class test_switch_player(unittest.TestCase):
    def setUp(self):
        self.game = Connect4()
                                                                                # forgot to set it up earlier, now its properly set up.
    def testing_switch_player(self):
        print(f"The player before the test is = {self.game.current_player}")    # was originally just checking the function,          
        self.game.switch_player()                                               # rather than within the context of the game
        self.assertEqual(self.game.current_player, 'O')

if __name__ == "__main__":
    unittest.main()

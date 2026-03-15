import unittest
from main import Connect4


class TestSwitchPlayer(unittest.TestCase):

    def test_switch_from_X_to_O(self):
        game = Connect4()
        game.current_player = 'X'

        game.switch_player()

        self.assertEqual(game.current_player, 'O')

    def test_switch_from_O_to_X(self):
        game = Connect4()
        game.current_player = 'O'

        game.switch_player()

        self.assertEqual(game.current_player, 'X')


if __name__ == "__main__":
    unittest.main()
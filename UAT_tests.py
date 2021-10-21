import unittest
from game import Game
from dice import Dice

class Tests(unittest.TestCase):

    # US1 
    # UAT1 - Initial position should be 1 for the player

    def test_initial_position(self):
        game = Game()
        self.assertEqual(game.player.position, 1, "Should be 1")

    # UAT2 - If on position 1 and moving 3 positions, should end up on position 4

    def test_move_3(self):
        game = Game()
        game.move(3)
        self.assertEqual(game.player.position, 4, "Should be 4")

    # UAT3 - If position 1, then roll 3, then roll 4, should be on position 8

    def test_move_8(self):
        game = Game()
        game.move(3)
        game.move(4)
        self.assertEqual(game.player.position, 8, "Should be 8")

    # US2
    # UAT1 - If on position 97 and rolling 3, win the game
    
    def test_win_from_97(self):
        game = Game(97)
        game.move(3)
        self.assertEqual(game.player.position, 100, "Should be 100")

    # UAT2 - If on position 97 and rolling 4, player stays on 97 and keeps rolling

    def test_overflow_from_97(self):
        game = Game(97)
        game.move(4)
        self.assertEqual(game.player.position, 97, "Should be 97")

    # US3
    # UAT1 Dice should always roll [1, 6]

    def test_dice_rolls(self):
        # simulating 1000 rolls to create a set of the rolls obtained, should be more than enough for a 6-faced dice
        rolls = []
        for _ in range(1000):
            rolls.append(Dice.roll_dice())
        rolls = set(rolls)
        self.assertEqual(rolls, {1, 2, 3, 4, 5, 6}, "Should be a set of {1, 2, 3, 4, 5, 6}")
        
    # UAT2 Given a roll of 4, token should move 4 positions ahead
    # Based on how I've designed the exercise, I believe US1-UAT2 covers this UAT, since it simulates a 
    # roll and checks the movement afterwards.

        
if __name__ == '__main__':
    unittest.main()

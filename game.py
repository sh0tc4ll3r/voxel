from player import Player
from dice import Dice
from board import Board

class Game:



    def __init__(self, initial_position=1):
        snakes = {16: 6,
                    46: 25,
                    49: 11,
                    62: 19,
                    64: 60,
                    74: 53,
                    89: 68,
                    92: 88,
                    95: 75,
                    99: 80
        }

        ladders = {2: 38,
                    7: 14,
                    8: 31,
                    15: 26,
                    28: 84,
                    36: 44,
                    51: 67,
                    71: 91,
                    78: 98,
                    87: 94,
                    }

        self.board = Board(snakes, ladders, 100)
        self.player = Player('Perico', initial_position)

    # adding posibility to force a roll to be able to test results
    def move(self, roll=-1):

        if roll == -1:
            roll = Dice.roll_dice()

        print(f'You roll {roll}!')

        potential_position = self.player.position + roll
        
        # check if player would go too far away on the board
        if potential_position > self.board.size: 
            print(f'Sorry {self.player.name} that would take you off the board. Try again.')
        # also check if the player has won with this move
        elif potential_position == self.board.size:
            self.player.move(self.board.size)
            print(f'Grats {self.player.name} you have won the game!')
            return False
        # otherwise check the players updated position after the move
        else:
            self.player.move(self.board.check_snake_or_ladder(potential_position))

        # small line to separate the rounds more clearly
        print("--------------------------------------")

        return True

        
if __name__ == '__main__':

    game = Game()
    rounds = 0

    while game.move():

        rounds += 1
        print(f'Round: {rounds}')


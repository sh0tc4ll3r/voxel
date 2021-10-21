import random

class Dice:

    # Using this as a static method since it won't really be used through an object
    @staticmethod
    def roll_dice():
        return random.randint(1,6)

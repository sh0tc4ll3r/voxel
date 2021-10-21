class Board:

    # Allowing for different board sizes and positions for snakes/ladders
    def __init__(self, snakes, ladders, size=100):
        self.size = size
        self.snakes = snakes
        self.ladders = ladders

    def check_snake_or_ladder(self, position):
        if position in self.snakes:
            print(f'Oh no! A snake takes you back to {self.snakes[position]}')
            return self.snakes[position]
        elif position in self.ladders:
            print(f'You are in luck, a ladder takes you straight to {self.ladders[position]}')
            return self.ladders[position]
        else:
            return position
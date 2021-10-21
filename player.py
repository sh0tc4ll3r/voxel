class Player:
    
    def __init__(self, name, initial_position):
        self.name = name
        self.position = initial_position

    def move(self, new_position):
        self.position = new_position
        print(f'{self.name} your new position is {self.position}')
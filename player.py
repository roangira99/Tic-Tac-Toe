import math
import random

# The player class is initialized with the letter that 
# The player is going to represent i.e x or o
class Player:
    def __init__(self, letter):
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass

# creating a random computer player class using inheritance
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        pass

# creating a human player class using inheritance
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

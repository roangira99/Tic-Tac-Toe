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
        # get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square

# creating a human player class using inheritance
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None # User hasn't input a value yet when starting the game
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            # checking whether input is a valid number that player can put in
            try:
                val = int(square) # If we can't cast the user input to an integer
                if val not in game.available_moves(): # If value given is not in the list of available moves
                    raise ValueError
                valid_square = True # If the above statements are successful, then the value is valid
            except ValueError: # catch the value error
                print('Invalid square. Try again')

        return val

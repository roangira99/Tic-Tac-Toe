import time
from player import HumanPlayer, RandomComputerPlayer
# Creating the Tic Tac Toe board class
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] # using a list of length 9 which represents the 3 x 3 board
        self.current_winner = None # keep track of winner

    def print_board(self):
        # getting the rows on the board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |' ) # join them in a string where the separators is the vertical line

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |' )

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
        # OR
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
        #     if spot == ' ':  # empty space
        #         moves.append(i) # append the index of the spot to moves since we want to know which empty spaces are available
        # return moves

    # funtion to check whether there are any empty sqaures on the bord
    def empty_squares(self):
        return ' ' in self.board # returns a boolean of whether or not there are empty spaces on the board
    
    # funtion that counts number of empty squares on the board
    def num_empty_squares(self):
        return self.board.count(' ')
    
    # defining a function to make a move!
    def make_move(self, square, letter):
        # if valid move then make move (assign square to letter) then return true
        # if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            # check whether there is a winner
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    # function to check for a winner
    def winner(self, square, letter):
        # winner if 3 in a row anywhere.. we have to check all of these
        # first let's check the row
        row_ind = square // 3 # the row its at
        row = self.board[row_ind*3 : (row_ind + 1) * 3] # getting a list of items in the row we've selected
        if all([spot == letter for spot in row]): # return true if everything in the row is equal to the letter
            return True
        
        # check column
        col_ind = square % 3 # the column we are in
        column = [self.board[col_ind+i*3] for i in range(3)] # for every single row (i) if we add the column index we get every single value in that column to get our column
        if all([spot == letter for spot in column]): # return true if everything in the column is equal to the letter
            return True
        
        # check diagonals
        # but only if the square is an even number (0, 2, 4, 6, 8)
        # these are the only moves possible to win in a diagonal
        if square % 2 ==0: # if the number is even
            diagonal1 = [self.board[i] for i in [0, 4, 8]] # left to right diagonal
            if all([spot == letter for spot in diagonal1]): # return true if everything in the column is equal to the letter
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] # right to left diagonal
            if all([spot == letter for spot in diagonal2]): # return true if everything in the column is equal to the letter
                return True
        # if all of these fail
        return False

def play(game, x_player, o_player, print_game=True): # print_game = True displays the steps when human player is playing against the computer
    #returns the winner of the game(the letter) or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    # winner determined by that which breaks the loop
    while game.empty_squares():
        # get move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # making a move
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board() # new representation of the board where this spot has now been claimed by the user
                print('')

            # if there is a current winner, end the game
            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # after a user has made a move, we need to alternate letters
            letter = 'O' if letter == 'X' else 'X' # switches players (condensed if-else statement)
            # could alternatively be written like this:
            # if letter == 'X
            #     letter = 'O'
            # else:
            #     letter = 'X'

        time.sleep(0.8) # add a delay before displaying opponent move

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = HumanPlayer('X') # aasign letter X to human player
    o_player = RandomComputerPlayer('O') # aasign letter O to computer player
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)


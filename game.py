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

    # funtion to check whether there are any ampty sqaures on the bord
    def empty_squares(self):
        return ' ' in self.board # returns a boolean of whether or not there are empty spaces on the board
    
    # funtion that counts number of empty squares on the board
    def num_empty_squares(self):
        return self.board.count(' ')

def play(game, x_player, o_player, print_game=True): # print_game = True displays the steps when human player is playing against the computer
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

        # defining a function to make a move!
        

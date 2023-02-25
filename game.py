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
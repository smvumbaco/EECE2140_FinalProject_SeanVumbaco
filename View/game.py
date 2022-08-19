import pickle
from View.coordinates import Coordinates

class Game:
    """
    Controls all the major functions of a game of sudoku
    """

    DIFFICULTIES = {'A': 36, 'B': 31, 'C': 26}

    def __init__(self, coords=Coordinates(), grid=None):
        """
        Constructor for Game object
        :param coords: Coordiates() object
        :param grid: Generator() object - don't define in arguments to avoid unnecessary processing
        """
        self.coords = coords
        self.grid = grid
        self.moves = 0

    def save_board(self):
        """
        Saves the current board under a file name specified by the user
        :return: None - just saves Generator() object to binary file
        """
        filename = input('Enter the name of the saved board: ')
        with open(filename, 'wb') as f:
            pickle.dump(self.grid, f)

    def load_board(self):
        """
        Pulls an existing Generator() object from a named file
        :return: Generator() object
        """
        while True:
            try:
                filename = input('Enter the name of the board to load in: ')
                with open(filename, 'rb') as f:
                    return pickle.load(f)
            except FileNotFoundError:
                print('Sorry! That file name is not recognized.\n')

    def negative_select(self, select):
        """
        Handles alternate yet anticipated user inputs
        Returns whether to cut out of the game or not
        :param select: int
        :return: boolean
        """
        if select == -1:
            return True
        elif select == -2:
            hint = self.grid.insert_hint()
            print(hint)
            return False
        elif select == -3:
            clue_row = self.coords.prompt_row()
            clue_col = self.coords.prompt_col()
            hint = self.grid.insert_hint(False, clue_row, clue_col)
            print(hint)
            return False
        else:
            self.save_board()
            return True

    def play_game(self):
        """
        Runs through game of sudoku
        Exits out if completed, saved, or manually quit by user
        :return: None
        """
        while self.grid.get_incomplete_grid() != self.grid.get_complete_grid():
            self.moves += 1
            print(f'\nMove {self.moves}')
            print('Enter X at any time to exit back to the main menu.')
            print('Enter Y at any time to plug in a random hint.')
            print('Enter Z at any time to request a specific hint.')
            print('Enter S at any time to save the current board to return to later.')
            print(self.grid)
            print('\n')
            row_select = self.coords.prompt_row()

            if row_select < 0:
                cancel = self.negative_select(row_select)
                if cancel:
                    break
                continue
            col_select = self.coords.prompt_col()
            if col_select < 0:
                cancel = self.negative_select(col_select)
                if cancel:
                    break
                continue
            num_select = self.coords.prompt_num()
            if num_select < 0:
                cancel = self.negative_select(num_select)
                if cancel:
                    break
                continue
            if self.grid.get_complete_grid()[row_select][col_select] != num_select:
                print('Number is not correct!')
            else:
                self.grid.plugin(row_select, col_select, num_select)
                print('Correct!')

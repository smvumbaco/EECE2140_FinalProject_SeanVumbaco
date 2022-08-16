import pickle


class Game:
    """
    Controls all the major functions of a game of sudoku
    """

    def __init__(self, coords, grid):
        self.coords = coords
        self.grid = grid

    def save_board(self):
        filename = input('Enter the name of the saved board: ')
        with open(filename, 'wb') as f:
            pickle.dump(self.grid, f)

    def load_board(self):
        while True:
            try:
                filename = input('Enter the name of the board to load in: ')
                with open(filename, 'rb') as f:
                    return pickle.load(f)
            except FileNotFoundError:
                print('Sorry! That file name is not recognized.\n')

    def play_game(self):
        moves = 1
        while self.grid.get_incomplete_grid() != self.grid.get_complete_grid():
            print(f'\nMove {moves}')
            print('Enter X at any time to exit back to the main menu.')
            print('Enter Y at any time to plug in a random hint.')
            print('Enter Z at any time to request a specific hint.')
            print('Enter S at any time to save the current board to return to later.')
            print(self.grid)
            print('\n')
            row_select = self.coords.prompt_row()
            if row_select < 0:
                if row_select == -1:
                    return
                elif row_select == -2:
                    hint = self.grid.insert_hint()
                    print(hint)
                elif row_select == -3:  # row_select == -3 -> specific hint
                    clue_row = self.coords.prompt_row()
                    clue_col = self.coords.prompt_col()
                    hint = self.board.insert_hint(False, clue_row, clue_col)
                    print(hint)
                else:
                    self.save_board()
                    break
                continue
            col_select = self.coords.prompt_col()
            if col_select < 0:
                if col_select == -1:
                    return
                elif col_select == -2:
                    hint = self.grid.insert_hint()
                    print(hint)
                elif col_select == -3:  # row_select == -3 -> specific hint
                    clue_row = self.coords.prompt_row()
                    clue_col = self.coords.prompt_col()
                    hint = self.insert_hint(False, clue_row, clue_col)
                    print(hint)
                else:
                    self.save_board()
                    break
                continue
            num_select = self.coords.prompt_num()
            if num_select < 0:
                if num_select == -1:
                    return
                elif num_select == -2:
                    hint = self.grid.insert_hint()
                    print(hint)
                elif num_select == -3:
                    clue_row = self.coords.prompt_row()
                    clue_col = self.coords.prompt_col()
                    hint = self.grid.insert_hint(False, clue_row, clue_col)
                    print(hint)
                else:
                    self.save_board()
                    break
                continue
            if self.grid.get_complete_grid()[row_select][col_select] != num_select:
                print('Number is not correct!')
            else:
                self.grid.plugin(row_select, col_select, num_select)
                print('Correct!')
            moves += 1

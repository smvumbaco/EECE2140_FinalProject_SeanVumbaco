from Model.generator import Generator
from View.menu import Menu
from View.coordinates import Coordinates
import pickle

# a = Grid()
# a.generate_solution(a.get_board())
# print(a)

# b = SudokuGenerator()

# a.generate_solution(a.get_board())

def play_game(coords, board):
    moves = 1
    while board.get_incomplete_grid() != board.get_complete_grid():
        print(f'\nMove {moves}')
        print('Enter X at any time to exit back to the main menu.')
        print('Enter Y at any time to plug in a random hint.')
        print('Enter Z at any time to request a specific hint.')
        print('Enter S at any time to save the current board to return to later.')
        print(board)
        print('\n')
        row_select = coords.prompt_row()
        if row_select < 0:
            if row_select == -1:
                return
            elif row_select == -2:
                hint = board.insert_hint()
                print(hint)
            elif row_select == -3: # row_select == -3 -> specific hint
                clue_row = coords.prompt_row()
                clue_col = coords.prompt_col()
                hint = board.insert_hint(False, clue_row, clue_col)
                print(hint)
            else:
                save_board(board)
                break
            continue
        col_select = coords.prompt_col()
        if col_select < 0:
            if col_select == -1:
                return
            elif col_select == -2:
                hint = board.insert_hint()
                print(hint)
            elif col_select == -3: # row_select == -3 -> specific hint
                clue_row = coords.prompt_row()
                clue_col = coords.prompt_col()
                hint = board.insert_hint(False, clue_row, clue_col)
                print(hint)
            else:
                save_board(board)
                break
            continue
        num_select = coords.prompt_num()
        if num_select < 0:
            if num_select == -1:
                return
            elif num_select == -2:
                hint = board.insert_hint()
                print(hint)
            elif num_select == -3:
                clue_row = coords.prompt_row()
                clue_col = coords.prompt_col()
                hint = board.insert_hint(False, clue_row, clue_col)
                print(hint)
            else:
                save_board(board)
                break
            continue
        if board.get_complete_grid()[row_select][col_select] != num_select:
            print('Number is not correct!')
        else:
            board.plugin(row_select, col_select, num_select)
            print('Correct!')
        moves += 1

def save_board(board):
    filename = input('Enter the name of the saved board: ')
    with open(filename, 'wb') as f:
        pickle.dump(board, f)

def load_board():
    while True:
        try:
            filename = input('Enter the name of the board to load in: ')
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print('Sorry! That file name is not recognized.\n')

if __name__ == '__main__':
    # c = Generator()
    # print(c)

    menu = Menu()
    coords = Coordinates()

    while True:

        menu_select = menu.prompt_menu()

        if menu_select == 'A':
            print('\n\n')
            fills = menu.prompt_difficulty()
            if fills == 0:
                continue
            game_grid = Generator(clues=fills)
            play_game(coords, game_grid)
            # print('Thank you for playing!')
        elif menu_select == 'B':
            game_grid = load_board()
            play_game(coords, game_grid)
            # print('Thank you for playing!')
        else:
            print('Thank you for playing!')
            break

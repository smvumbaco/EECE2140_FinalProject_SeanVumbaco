from Model.generator import Generator
from View.game import Game
from View.menu import Menu
from View.coordinates import Coordinates
import pickle

# a = Grid()
# a.generate_solution(a.get_board())
# print(a)

# b = SudokuGenerator()

# a.generate_solution(a.get_board())

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
            game = Game(coords, game_grid)
            game.play_game()
        elif menu_select == 'B':
            game = Game()
            game_grid = game.load_board() # Serious problems here
            game = Game(coords, game_grid)
            game.play_game()
            # print('Thank you for playing!')
        else:
            print('Thank you for playing!')
            break

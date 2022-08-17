class Coordinates:
    """
    Class whose methods handle user input for selecting rows and columns in sudoku grid
    """

    COL_DICT = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'X': -1, 'Y': -2, 'Z': -3, 'S': -4}
    ROW_DICT = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'X': -1, 'Y': -2, 'Z': -3, 'S': -4}

    def __init__(self, row_num=0, col_num=0, digit=0):
        """
        Constructor for Coordinates() object
        :param row_num: int
        :param col_num: int
        :param digit: int
        """
        self.row_num = row_num
        self.col_num = col_num
        self.digit = digit

    def prompt_row(self):
        """
        Get a row number from the user - handle inappropriate input
        :return: int - index of row
        """
        while True:
            try:
                row = input('Select a row: ')[0].upper()
                return Coordinates.ROW_DICT[row]
            except KeyError:
                print('Invalid row selection. Please try again.')
            except IndexError:
                print('Input must not be blank.')

    def prompt_col(self):
        """
        Get a column letter from the user - handle inappropriate input
        :return: int - index of column
        """
        while True:
            try:
                col = input('Select a column: ')[0].upper()
                return Coordinates.COL_DICT[col]
            except KeyError:
                print('Invalid column selection. Please try again.')
            except IndexError:
                print('Input must not be blank.')

    def prompt_num(self):
        """
        Get a plugin number from the user - handle inappropriate input
        Does not handle ints outside 1-9 here - that is screened out by Game() play_game() function
        :return: int
        """
        while True:
            try:
                num = input('Enter a digit to insert: ')[0]
                digit = int(num)
                return digit
            except ValueError:
                if num.upper() == 'X':
                    return -1
                elif num.upper() == 'Y':
                    return -2
                elif num.upper() == 'Z':
                    return -3
                else:
                    print('Invalid digit entry. Please try again.')
            except IndexError:
                print('Input must not be blank.')



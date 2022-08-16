from Model.square import Square
from random import randint

class Grid:
    """
    As of right now, basically just establishes variables that are consistent with all created sudoku boards
    """

    NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    BLOCK1 = [(i, j) for i in range(3) for j in range(3)]
    BLOCK2 = [(i, j) for i in range(3) for j in range(3, 6)]
    BLOCK3 = [(i, j) for i in range(3) for j in range(6, 9)]
    BLOCK4 = [(i, j) for i in range(3, 6) for j in range(3)]
    BLOCK5 = [(i, j) for i in range(3, 6) for j in range(3, 6)]
    BLOCK6 = [(i, j) for i in range(3, 6) for j in range(6, 9)]
    BLOCK7 = [(i, j) for i in range(6, 9) for j in range(3)]
    BLOCK8 = [(i, j) for i in range(6, 9) for j in range(3, 6)]
    BLOCK9 = [(i, j) for i in range(6, 9) for j in range(6, 9)]

    ALL_BLOCKS = [BLOCK1, BLOCK2, BLOCK3, BLOCK4, BLOCK5, BLOCK6, BLOCK7, BLOCK8, BLOCK9]

    EMPTY_GRID = [[0 for i in range(9)] for j in range(9)]
    ALL_POSITIONS = [(i, j) for i in range(9) for j in range(9)]

    '''
    def __init__(self, grid=[[0 for i in range(9)] for j in range(9)], clues=36,
                 unfilled=[(i, j) for i in range(9) for j in range(9)],
                 filled=list(), curr_row=0, curr_col=0):
        """ Constructor, mostly used to initialize difficulty of board (# of clues) """
        self.grid = grid
        self.clues = clues # Easy: 36, Medium: 31, Hard: 26
        self.unfilled = unfilled
        self.filled = filled # May be used for better efficiency
        self.curr_row = curr_row
        self.curr_col = curr_col
    '''

#
#     @staticmethod
#     def shuffle_list():
#         ref = Grid.NUMS
#         rands = list()
#         while len(ref) > 0:
#             num = ref[randint(0, len(ref) - 1)]
#             rands.append(num)
#             ref.remove(num)
#         return rands
#
#     def make_empty_board(self):
#         """ Creates a sudoku board of all zeros (do not appear) """
#         # fill = list()
#         self.unfilled = [(i, j) for i in range(9) for j in range(9)]
#         self.filled = list()
#         self.board = [[0] * 9 for i in range(9)]
#         for i in range(0, 9):
#             for j in range(0, 9):
#                 self.board[i][j] = Square(0, (i, j))
#
#     def __str__(self):
#         """ Returns the sudoku board in a user-friendly format """
#         cols = '    A  B  C   D  E  F   G  H  I'
#         border = '   ------------------------------'
#         output = cols + '\n' + border + '\n'
#         for i in range(0, 9):
#             if i == 3 or i == 6:
#                 output += border + '\n'
#             output += str(i+1) + ' } '
#             for j in range(0, 9):
#                 if j == 2 or j == 5 or j == 8:
#                     buffer = ' | '
#                 else:
#                     buffer = '  '
#                 if self.board[i][j] == 0:
#                     num = ' '
#                 else:
#                     num = str(self.board[i][j])
#                 output += num + buffer
#             if i < 8:
#                 output += '\n'
#         output += '\n' + border
#         return output
#
#         # def row_conflict(self, square, row, num): # Simplify to not include square
#
#     def row_conflict(self, row, num):
#         """ Returns whether there is a conflict in the row specified """
#         for i in range(9):
#             # if i != square.get_col and num == self.board[row][i].get_num(): # Eliminate col of square and check if num is already in row
#             if self.board[row][i] == num:
#                 print(f'Row conflict in row {row} with number {num}')
#                 return True
#         return False
#
#         # def col_conflict(self, square, col, num): # Simplify to not include square
#
#     def col_conflict(self, col, num):
#         """ Returns whether there is a conflict in the column specified """
#         for i in range(9):
#             # if i != square.get_row and num == self.board[i][col].get_num(): # Eliminate row of square and check if num is already in col
#             if self.board[i][col] == num:
#                 print(f'Column conflict in col {col} with number {num}')
#                 return True
#         return False
#
#         # def block_conflict(self, square, num): # Simplify to not include square
#
#     def block_conflict(self, row, col, num):
#         """ Returns whether there is a conflict for the block of square """
#         for block in Grid.ALL_BLOCKS:
#             if (row, col) in block:  # Narrow down block
#                 for spot in block:
#                     # if (not (square == self.board[spot[0]][spot[1]])) and (num == self.board[spot[0]][spot[1]].get_num()): # Different POSITION, same NUM
#                     if self.board[row][col] == num:
#                         print(f'Block conflict in block {block} with number {num}')
#                         return True
#         return False
#
#     '''
#     def conflict(self, square, row, col, num):
#         return self.row_conflict(square, row, num) or self.col_conflict(square, col, num) or self.block_conflict(square, num)
#     '''
#
#     def conflict(self, row, col, num):
#         return self.row_conflict(row, num) or self.col_conflict(col, num) or self.block_conflict(row, col, num)
#
#     def generate_board(self):
#         """ Creates a potential sudoku board... must be verified as solvable with unique solution """
#         '''
#         self.fill_random_spot(first=True)
#         clues = self.clues-1
#         while clues > 0:
#             insert = self.fill_random_spot(first=False)
#             if insert:
#                 clues -= 1
#         '''
#         for row in range(9):
#             nums = Grid.shuffle_list()
#             print(f'Row: {row}')
#             # print(nums)
#             for col in range(9):
#                 print(f'Column: {col}')
#                 if self.empty_spot(row, col):
#                     for num in nums:
#                         # print(num)
#                         if not self.conflict(self.board[row][col], row, col, num):
#                             self.plugin(num, (row, col))
#                             if row == 8 and col == 8:
#                                 return True
#                             elif self.generate_board():
#                                 return True
#                     # break
#                 # break
#         self.wipe((row, col))
#         return False
#
#     def generate_solution(self, grid):
#         """generates a full solution with backtracking"""
#         # number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#         for i in range(0, 81):
#             row = i // 9
#             col = i % 9
#             # find next empty cell
#             # if self.board[row][col] == 0:
#             if grid[row][col] == 0:
#                 number_list = Grid.shuffle_list()
#                 # shuffle(number_list)
#                 for number in number_list:
#                     if not self.conflict(row, col, number): # if self.valid_location(grid, row, col, number):
#                         # self.path.append((number, row, col))
#                         grid[row][col] = number
#                         # self.board[row][col] = number
#                         # if not self.find_empty_square(grid):
#                         if not self.find_empty_spot():
#                             return True
#                         else:
#                             # if self.generate_solution():
#                             if self.generate_solution(grid):
#                                 # if the grid is full
#                                 return True
#                 break
#         grid[row][col] = 0
#         # self.wipe(row, col)
#         return False
#
#     def fill_random_spot(self, first):
#         """ Fills a random spot on self.board with a random integer 1-9 and returns True
#         OR notices a conflict (row, column, or block) and returns false """
#         rand = randint(1, 9)
#         random_index = randint(0, len(self.unfilled) - 1)
#         spot = self.unfilled[random_index]
#         row, col = spot[0], spot[1]
#         if first:
#             self.plugin(rand, spot, solving=False)
#             return True
#         else:
#             square = self.board[row][col]
#             if self.conflict(square, row, col, rand):
#                 return False
#             else:
#                 self.plugin(rand, spot, solving=False)
#                 return True
#
#     def plugin(self, num, position, solving=True):
#         self.board[position[0]][position[1]].set_num(num)
#         if not solving:
#             self.unfilled.remove(position)
#             self.filled.append(position)
#
#     def wipe(self, row, col):
#         # self.board[position[0]][position[1]].set_num(0)
#         self.board[row][col] = 0
#
#     def get_unfilled(self):
#         return self.unfilled
#
#     def get_filled(self):
#         return self.filled
#
#     def get_board(self):
#         return self.board
#
#     # Helper function for solve
#     def find_empty_spot(self):
#         for i in range(9):
#             for j in range(9):
#                 if self.empty_spot(i, j):
#                     self.curr_row = i
#                     self.curr_col = j
#                     return True
#         return False
#
#     def empty_spot(self, row, col):
#         # return self.board[row][col].get_num() == 0
#         return self.board[row][col] == 0
#
#     def solve(self, rand=False):
#
#         # No empty spots - completed!
#         if not self.find_empty_spot():
#             return True
#
#         row = self.curr_row
#         col = self.curr_col
#         square = self.board[row][col] # This might be a potential source of error!!! Consider changing later
#
#         for num in range(1, 10): # Iterate from 0 to 9
#
#             if rand:
#                 num = randint(1, 9)
#
#             # If looks good
#             if not self.conflict(square, row, col, num):
#
#                 # Tentative assignment
#                 self.board[row][col].set_num(num)
#
#                 if self.solve():
#                     return True
#
#                 # No bueno - set back to 0
#                 self.wipe((row, col))
#
#         return False
#
#
# '''
#     def solve(self, start=(0, 0), backing=False):
#         print(self)
#         if start == (0, 0):
#             start = self.unfilled[0]
#         eligible = self.unfilled[self.unfilled.index(start):]
#         solved = False
#         while not solved:
#             for spot in eligible:
#                 row, col = spot[0], spot[1]
#                 square = self.board[row][col]
#                 start_num = square.get_num() + 1
#                 if backing:
#                     self.wipe(start)  # Set value of current index to 0
#                 for i in range(start_num-1, 9):
#                     if self.conflict(square, row, col, i+1):
#                         # self.board[row][col].del_potential(i+1)
#                         if i < 8:
#                             continue # Skip to next num
#                         else: # IMPOSSIBLE TO INSERT ANYTHING 1-9
#                             self.solve(start=self.unfilled[self.unfilled.index(spot) - 1], backing=True)
#                     # elif i+1 in self.board[row][col].get_potentials():
#                     else:
#                         self.plugin(i+1, spot)
#                         print(f'Plugged in {i+1} at spot {spot}')
#                         if spot == (8, 8):
#                             print('Completed!!!!!!!')
#                             solved = True # ONLY solved if final index reached!
#                         break
# '''
#


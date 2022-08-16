from Model.grid import Grid
from random import randint
from random import shuffle
from copy import deepcopy
from View.coordinates import Coordinates

class Generator:
	"""
	Contains 3 main functions (assisted by helper functions, of course):
	1. make_full_grid(): Creates a completed 9x9 Sudoku board
	2. make_playable_grid(): Creates a playable Sudoku board whose only solution is given by 1.
	3. solve(): Determines whether a given board is solvable - COUNTS number of solutions
	"""

	def __init__(self, grid=None, clues=36):
		"""
		Constructor for Generator class. Main attributes are
		complete_grid - filled out sudoku board
		incomplete_grid - playable board presented to player
		:param grid: 2D array (list of lists)
		:param clues: integer
		"""
		self.complete_grid = Grid.EMPTY_GRID
		# self.filled = Grid.ALL_POSITIONS -- This isn't working for some reason.
		self.filled = [(i, j) for i in range(9) for j in range(9)]
		self.unfilled = list()
		self.clues = clues # How many values need to be left in playable grid

		self.make_full_grid() # Fill out self.complete_grid()

		self.incomplete_grid = deepcopy(self.complete_grid) # MUST make deepcopy - object of objects
		self.make_playable_grid()

	def get_incomplete_grid(self):
		return self.incomplete_grid

	def get_complete_grid(self):
		return self.complete_grid

	@staticmethod # Does not work... :( alternate method for shuffling digits 1-9
	def shuffle_list():
		ref = Generator.NUMS
		rands = list()
		while len(ref) > 0:
			num = ref[randint(0, len(ref) - 1)]
			rands.append(num)
			ref.remove(num)
		return rands

	def __str__(self):
		# Printing out complete grid and incomplete grid very useful for debugging!!!
		# output = self.string_grid(self.complete_grid) + '\n\n\n' + self.string_grid(self.incomplete_grid)
		output = self.string_grid(self.incomplete_grid)
		return output

	def string_grid(self, grid):
		""" Returns the sudoku board in a user-friendly format """
		cols = '    A  B  C   D  E  F   G  H  I'
		border = '   ------------------------------'
		output = cols + '\n' + border + '\n'
		for i in range(0, 9):
			if i == 3 or i == 6:
				output += border + '\n'
			output += str(i + 1) + ' } '
			for j in range(0, 9):
				if j == 2 or j == 5 or j == 8:
					buffer = ' | '
				else:
					buffer = '  '
				if grid[i][j] == 0:
					num = ' '
				else:
					num = str(grid[i][j])
				output += num + buffer
			if i < 8:
				output += '\n'
		output += '\n' + border
		return output

	def plugin(self, row, col, num):
		self.incomplete_grid[row][col] = num

	def insert_hint(self, rand=True, row_select=0, col_select=0):
		if rand:
			spot = self.unfilled[randint(0, len(self.unfilled) - 1)]
			row, col = spot[0], spot[1]
			# Must get row and column KEYS from value
			for label in Coordinates.ROW_DICT:
				if Coordinates.ROW_DICT[label] == row:
					row_label = label
			for key, value in Coordinates.COL_DICT.items():
				if value == col:
					col_label = key
			num = self.complete_grid[row][col]
			self.incomplete_grid[row][col] = num
		else:
			# row, col = Coordinates.ROW_DICT[row_label], Coordinates.COL_DICT[col_label]
			for label in Coordinates.ROW_DICT:
				if Coordinates.ROW_DICT[label] == row_select:
					row_label = label
			for key, value in Coordinates.COL_DICT.items():
				if value == col_select:
					col_label = key
			num = self.complete_grid[row_select][col_select]
			self.incomplete_grid[row_select][col_select] = num
		return f'Inserted {num} at row {row_label}, column {col_label}'

	def row_conflict(self, grid, row, num):
		""" Returns whether there is a conflict in the row specified """
		for i in range(9):
			if grid[row][i] == num:
				return True
		return False

	def col_conflict(self, grid, col, num):
		""" Returns whether there is a conflict in the column specified """
		for i in range(9):
			if grid[i][col] == num:
				return True
		return False

	def block_conflict(self, grid, row, col, num):
		""" Returns whether there is a conflict for the block of square """
		for block in Grid.ALL_BLOCKS:
			if (row, col) in block:  # Narrow down block
				for spot in block:
					# if (not (square == self.board[spot[0]][spot[1]])) and (num == self.board[spot[0]][spot[1]].get_num()): # Different POSITION, same NUM
					if grid[spot[0]][spot[1]] == num:
						# print(f'Block conflict in block {block} with number {num}')
						return True
		return False

	def conflict(self, grid, row, col, num):
		return self.row_conflict(grid, row, num) or self.col_conflict(grid, col, num) or self.block_conflict(grid, row, col, num)

	def find_empty_spot(self, grid):
		for i in range(9):
			for j in range(9):
				if grid[i][j] == 0:
					self.curr_row = i # Used in solve()
					self.curr_col = j
					return True
		return False

	def solve(self, grid):
		"""solve a given sudoku puzzle with backtracking"""
		for i in range(81):
			row = i // 9
			col = i % 9
			if grid[row][col]==0: # If not, go to next position
				for num in range(1,10):
					if not self.conflict(grid, row, col, num):
						grid[row][col] = num
						if not self.find_empty_spot(grid):
							self.solutions += 1
							break # Go to next position
						else:
							if self.solve(grid):
								return True
				break
		grid[row][col]=0  
		return False

	def make_full_grid(self):
		"""generates a full solution with backtracking"""
		# num_list = Generator.NUMS
		# print('Making full grid')
		for i in range(81):
			row = i // 9
			col = i % 9
			# Investigate current square (if equal to 0) - else, move to next one
			if self.complete_grid[row][col] == 0:
				shuffle(Grid.NUMS)
				# nums = Generator.shuffle_list() < this doesn't work... appears to be remedied by random.shuffle() method
				for num in Grid.NUMS:  # CHOOSE a random int to go in square
					# if self.valid_location(self.complete_grid, row, col, number):  # If valid, ASSIGN number
					if not self.conflict(self.complete_grid, row, col, num):
						self.complete_grid[row][col] = num
						if not self.find_empty_spot(self.complete_grid): # SUCCESS! self.complete_grid is filled out
							return True
						else:
							if self.make_full_grid(): # Recursive step: base case is find_empty_spot function
								# if the grid is full
								return True
				break # Exhausted every num in Generator.NUMS & all invalid - have to start backtracking
		# ONLY reaches here if plugging in was UNSUCCESSFUL - must blank out and keep trying random numbers
		self.complete_grid[row][col] = 0
		return False

	def make_playable_grid(self):
		empties = 0
		while empties < 81 - self.clues:
			spot = self.filled[randint(0, len(self.filled) - 1)]
			row, col = spot[0], spot[1]
			val = self.incomplete_grid[row][col]
			self.incomplete_grid[row][col] = 0
			temp_grid = deepcopy(self.incomplete_grid)

			self.solutions = 0

			self.solve(temp_grid)
			if self.solutions == 1:
				empties += 1
				self.filled.remove(spot)
				self.unfilled.append(spot)
			else: # Add val back in
				self.incomplete_grid[row][col] = val

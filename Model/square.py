class Square:

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

    def __init__(self, num, position, potentials=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
        self.num = num
        self.position = position
        self.potentials = potentials
        for item in Square.ALL_BLOCKS:
            if position in item:
                self.block = Square.ALL_BLOCKS.index(item) + 1
        # print(num, self.num)

    def __str__(self):
        if self.num == 0:
            return ' '
        return str(self.num)

    def __eq__(self, other):
        """ Returns whether 2 squares have the same position (open to change later) """
        return self.position == other.position

    def conflict(self, other):
        """ Determines the equivalence of the num attribute of 2 square objects """
        return self.num == other.num

    def add_potential(self, num):
        if num not in self.potentials:
            self.potentials.add(num)

    def del_potential(self, num):
        if num in self.potentials:
            self.potentials.remove(num)

    def get_potentials(self):
        return self.potentials

    def get_block(self):
        return self.block

    def get_num(self):
        return self.num

    def set_num(self, val):
        self.num = val

    def get_position(self):
        return self.position

    def get_row(self):
        return self.position[0]

    def get_col(self):
        return self.position[1]

    def filled(self):
        """ Returns whether a square is filled or not """
        if self.num != 0:
            return True
        return False


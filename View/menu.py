class Menu:

    def __init__(self, play_recall='', fillin=0):
        """
        Constructor for Menu object - just needed to set up attributes
        :param play_recall: string - User entry to play, recall a grid, or exit the game
        :param fillin: int - Number of clues (difficulty)
        """
        self.play_recall = play_recall
        self.fillin = fillin

    def prompt_menu(self):
        """
        Handles user input for the main menu of the game
        :return: string
        """
        while True:
            print('\nWelcome to All About Sudoku! Please choose an option from below:', '\n',
                  'A: Play a new game', '\n',
                  'B: Recall an existing game', '\n',
                  'C: Terminate game', sep='')
            selection = input('Entry: ')
            try:
                if selection.upper()[0] == 'A':
                    self.play_recall = 'A'
                    return self.play_recall
                elif selection.upper()[0] == 'B':
                    self.play_recall = 'B'
                    return self.play_recall
                elif selection.upper()[0] == 'C':
                    self.play_recall = 'C'
                    return self.play_recall
                else:
                    print('Input not recognized. Please try again!\n')
            except IndexError:
                print('Input must not be blank.\n')

    def prompt_difficulty(self):
        """
        Handles the user input for selecting a grid difficulty (number of clues)
        :return: int
        """
        while True:
            difficulty = input('Please select a difficulty: \n' +
                               'A: Easy \n' +
                               'B: Medium \n' +
                               'C: Hard \n' +
                               'D: Return to Main Menu \n' +
                               'Entry: ')
            try:
                if difficulty.upper()[0] == 'A':
                    self.fillin = 36
                    return self.fillin
                elif difficulty.upper()[0] == 'B':
                    self.fillin = 31
                    return self.fillin
                elif difficulty.upper()[0] == 'C':
                    self.fillin = 26
                    return self.fillin
                elif difficulty.upper()[0] == 'D':
                    return 0
                else:
                    print('Input not recognized. Please try again!\n')
            except IndexError:
                print('Input must not be blank.\n')
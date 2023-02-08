'''
Practice
'''

# Import List
from typing import List 

# Main function
def validate_board(board: List) -> bool:
    '''
    Checks if field is ready for play
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 7****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    >>> validate_board('Hello, world!')
    False
    >>> validate_board(["**** ****", "***11****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   7  **", "  8  2***","  2  ****"])
    False
    >>> validate_board(["**** ****", "***  ****", "**  *****", "* *  ****", "     * * ", " *  **  *", "       **", "  *   ***","  *  ****"])
    True
    '''

    if not isinstance(board, list):
        return False

    board_length = len(board)
    reversed_board = [''] * board_length

    for line in board:
        for el in line:
            if el != ' ' and el != '*' and line.count(el) > 1:
                return False

    for j in range (0, board_length):
        for t in range (0, board_length):
            reversed_board[j] += board[t][j]

    for row in reversed_board:
        for elem in row:
            if elem != ' ' and elem != '*' and row.count(elem) > 1:
                return False

    return True


if __name__ == '__main__':

    import doctest
    doctest.testmod(verbose = True)
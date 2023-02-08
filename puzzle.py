'''
Practice
'''

def validate_board(board):
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


    return True


def check_rows(board: list) -> bool:
    for elem in board:
        row = [block for block in elem if block.isnumeric()]
        if len(set(row)) != len(row):
            return False

    return True


def check_columns(board: list) -> bool:
    for num in range(len(board)):
        column = [row[num] for row in board if row[num].isnumeric()]
        if len(set(column)) != len(column):
            return False

    return True


def check_colored(board: list) -> bool:
    coord = [len(board) - 1, 0]
    for num in range(5):
        elem = [board[coord[0] - i][coord[1]] for i in range(5) if board[coord[0] - i][coord[1]].isnumeric()] +\
            [board[coord[0]][coord[1] + j] for j in range(5) if board[coord[0]][coord[1] + j].isnumeric()]
        if len(set(elem)) != len(elem):
            return False

    return True


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())

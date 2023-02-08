def validate_board(board):
    '''
    board = [
 "**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]
    '''
    #check rows
    for elem in board:
        row = [block for block in elem if block.isnumeric()]
        if len(set(row)) != len(row):
            return False
    
    #check columns
    for num in range(len(board)):
        column = [row[num] for row in board if row[num].isnumeric()]
        if len(set(column)) != len(column):
            return False
    

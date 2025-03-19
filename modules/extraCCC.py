numChances = 7

def wrapBoard(board):
    rowOfNums = []
    
    #creating a row of nums of length board to latter insert
    for i in range(board):
        rowOfNums[i] = i
    
    board.insert(0, rowOfNums)
    

def printBoard(board):
    for index, ele in enumerate(board):
        print(f'{"%% %%", index-1, ele}')

def beginGame(board):
    chances = numChances
    chancesLeft = numChances
    for i in range(chances):
        print(f'{"Input coordinate. You have %% chances left" ,chancesLeft }')
        printBoard(board)
        --chancesLeft
        
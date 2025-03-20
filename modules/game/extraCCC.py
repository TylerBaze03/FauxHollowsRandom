from modules import boardGen
from copy import deepcopy

chars = ['@', '#', '!', 'O', '*']
numChances = 7



def printBoard(board):
    
    for index, ele in enumerate(board):
        print(index+1, *ele)

#string that builds the finishing message
def congratsStringBuilder(piecesObtained):
    retString = 'All out chances!\nYou obtained ' + str(piecesObtained[0]) +' scissors pieces, ' + str(piecesObtained[1]) + ' present pieces, and ' + str(piecesObtained[2]) + ' Faux piece.\n'
    retString += "Congrats! You "
    
    
    if(piecesObtained[0] == 6):
        retString+= "obtained all parts to the scissors "
    if(piecesObtained[1] == 4):
        if(piecesObtained[0] == 6):
            retString+= "and "
        retString+= "obtained all parts to the present"
    if(piecesObtained[2] == 1):
        if(piecesObtained[0] == 6 or (piecesObtained[1] == 4)):
            retString+= "and"
        retString+= "obtained the Faux!"
    if(piecesObtained[0] < 6 and piecesObtained[1] < 4 and piecesObtained[2] < 1):
        retString+= "tried your best"
    return retString


#loops through both boards and ads to 2 arrays and 1 var names FauxGet, if the 2 arrays both have the correct amount they have obtained that item
#if FauxGet is equal to 0 they did not find him if it is equal to 1 they did 
#returns a list of the how many items from each they got [scissors peices, present peices, fauxVar]
def compareBoards(userBoard, keyBoard):
    sTotal = 0
    pTotal = 0
    fauxVar = 0
    for i in range(boardGen.boardDim):
        for j in range(boardGen.boardDim):
            if keyBoard[i][j] != 'X' and userBoard[i][j] == keyBoard[i][j] and keyBoard[i][j] != 'O' and keyBoard[i][j] != '@':
                #scissors peice
                if userBoard[i][j] == '#':
                    sTotal += 1
                #present peice
                elif userBoard[i][j] == '!':
                    pTotal += 1
                #theFaux!!
                else:
                    fauxVar += 1
    
    totals = [sTotal, pTotal, fauxVar]
    return totals

def beginGame():
    keyAndVal = boardGen.generateboard()
    key = keyAndVal[0]
    baseBoard = keyAndVal[1]
    xBar = [i for i in range(boardGen.boardDim +1 )]
    
    chances = numChances
    chancesLeft = numChances
    print(f'Input coordinates [x,y]. You have {chancesLeft} chances left: ')
    printBoard(baseBoard)
    print(*xBar)
    print("\n")
    #remeber x is your row and y is you collumn
    for i in range(chances):
        userInRow = 0
        userInCol = 0
        
        
        #whether or not an input was corectly taken in 0 no, 1 yes
        sInput = 0
        
        while sInput == 0:
            userInCol = input("X: ")
            userInCol = int(userInCol) -1
            if(int(userInCol) > boardGen.boardDim or int(userInCol) < 0):
                print("Enter a valid coordinate\n")
            else:
                userInRow = input("Y: ")
                userInRow = int(userInRow) -1
                if(int(userInRow) > boardGen.boardDim or int(userInRow) < 0):
                    print("Enter a valid coordinate\n")
                elif(baseBoard[userInRow][userInCol] in chars):
                    print("Enter a valid coordinate\n")
                else:
                    sInput = 1
        #"O means the user has tried this area"
        if key[userInRow][userInCol] == 'X':
            baseBoard [userInRow][userInCol] = 'O'
        else:
            baseBoard[userInRow][userInCol] = key[userInRow][userInCol]
        chancesLeft -= 1
        print(f'Input coordinates [x,y]. You have {chancesLeft} chances left: ')
        printBoard(baseBoard)
        print(*xBar)
        print("\n")
    
    piecesObtained = compareBoards(baseBoard, key)
    
    gzStr = congratsStringBuilder(piecesObtained)
    
    print(gzStr)
    
beginGame()
    
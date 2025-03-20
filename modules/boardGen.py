import random
import time
from copy import deepcopy


# # == to scissors, @ == unplaceable, ! == to present, X == placeable, * == faux
#['X','X','X','X','X','X'],
#['X','X','@','X','X','X'],
#['X','X','X','X','@','X'],
#['X','X','X','X','X','@'],
#['X','@','X','X','X','X'],
#['X','X','X','@','X','X']

#['X','X','@','X','X','X']
#['X','X','X','X','@','X'],
#['X','X','X','X','X','X'],
#['X','X','X','X','X','X'],
#['X','X','X','X','@','X'],
#['X','@','X','X','X','X'],


#Now start the present case than actually taking inoput from user
# todo:
#Finish BFS and try ang et it to work, if not, if statements it is:(
#if bfs is do able, fix the gen board function than test test test
#x and y are swapped but its too far in to fix this :(


testVar = 0


boardDim = 6
BOARD1 = [['X','X','X','X','X','X'],['X','X','@','X','X','X'],['X','X','X','X','@','X'],['X','X','X','X','X','@'],['X','@','X','X','X','X'],['X','X','X','@','X','X']]
BOARD2 = [['X','X','@','X','X','X'],['X','X','X','X','@','X'],['X','X','X','X','X','X'],['X','X','X','X','X','X'],['X','X','X','X','@','X'],['X','@','X','X','X','X']]
ALLBOARDS = [BOARD1, BOARD2]
#list of what you dont want to overwrite
nonos = ['@', '#', '!']

#dfs cords for scissors
    #        0 1  2  3 4  5  6  7  8  9  10 11 12 13 14 15 16  17  18  19  20
CORDSROWSCI = [0,-1,-1,0,1, 1, 1, 0,-1,-2,-2,-2,-1, 0, 1, 2, 2,  2,  1,  0, -1]
CORDSCOLSCI = [0,0 , 1,1,1, 0,-1,-1,-1,-1, 0, 1, 2, 2, 2, 1, 0, -1, -2, -2, -2]

#dfs coords for present
    #        0 1  2  3 4  5  6  7  8
CORDSROWPRES = [0,-1,-1,0,1, 1, 1, 0,-1]
CORDSCOLPRES = [0, 0, 1,1,1, 0,-1,-1,-1]

#shouldnt be used outside of testing this specific py file
def printBoard(playBoard):
    for count, ele in enumerate(playBoard):
        print(count, ele)


#this should really be rewritten      
#vis = [[False for i in range(boardDim)] for j in range(boardDim)]


#Creates a used array of all visited points around the vertex than allows us to creates the object based off of it
#Figure 1 Scissors Search Area
#    9  10 11
#20  8  1  2  12
#19  7  0  3  13
#18  6  5  4  14
#    17 16 15 


#legend:
#the numbers above each if statement tell which statement it is checking for whithin the above figure
def makeSci (x,y,playBoard):
    visitedSci = [False for i in range(len(CORDSROWSCI))]
    vertex = playBoard[x][y]
    #first checking the input given and returning immedietly
    if vertex in nonos:
        return -1
    else:
        visitedSci[0] = True
    #for loop to fill the vis array 
    for i in range(len(CORDSROWSCI)-1):
        if ((x + CORDSROWSCI[i]) >= boardDim or (x + CORDSROWSCI[i]) < 0 or (y + CORDSCOLSCI[i]) >= boardDim or (y + CORDSCOLSCI[i]) < 0):
            visitedSci[i] = False
        else:
            vertex = playBoard[x+CORDSROWSCI[i]][y + CORDSCOLSCI[i]]
            if vertex in nonos:
                visitedSci[i] = False
            else:
                visitedSci[i] = True
    #0,1,2,3
    if (visitedSci[1] != False != False and visitedSci[2] != False != False and visitedSci[3] != False):
        #10,11
        if(visitedSci[10] != False and visitedSci[11] != False):
            playBoard[x][y] = "#"      #0
            playBoard[x-1][y] = "#"    #1
            playBoard[x-1][y+1]= "#"   #2
            playBoard[x][y+1]= "#"     #3
            playBoard[x-2][y] = "#"    #10
            playBoard[x-2][y+1] = "#"   #11
            return playBoard
        #12,13
        
        elif(visitedSci[12] != False and visitedSci[13] != False):
            playBoard[x][y] = "#"      #0
            playBoard[x-1][y] = "#"    #1
            playBoard[x-1][y+1]= "#"   #2
            playBoard[x][y+1]= "#"     #3
            playBoard[x-1][y+2] = "#"  #12
            playBoard[x][y+2] = "#"    #13
            return playBoard
    
    #0,3,4,5
    if(visitedSci[3] != False and visitedSci[4] != False and visitedSci[5] != False):
        #13,14
        if(visitedSci[13] != False and visitedSci[14] != False):
            playBoard[x][y]= "#"       #0
            playBoard[x][y+1]= "#"     #3
            playBoard[x+1][y+1]= "#"   #4
            playBoard[x+1][y]= "#"     #5 
            playBoard[x][y+2] = "#"    #13
            playBoard[x+1][y+2] = "#"  #14
            return playBoard
        #15,16
        elif(visitedSci[15] != False and visitedSci[16] != False):
            playBoard[x][y]= "#"       #0
            playBoard[x][y+1]= "#"     #3
            playBoard[x+1][y+1]= "#"   #4
            playBoard[x+1][y]= "#"     #5 
            playBoard[x+2][y+1] = "#"  #15
            playBoard[x+2][y] = "#"    #16
            return playBoard
    #0,5,6,7
    if(visitedSci[5] != False and visitedSci[6] != False and visitedSci[7] != False ):
        #16,17
        if(visitedSci[16] != False and visitedSci[17] != False):
            playBoard[x][y] = "#"      #0
            playBoard[x+1][y] = "#"    #5
            playBoard[x+1][y-1]= "#"   #6
            playBoard[x][y-1] = "#"    #7
            playBoard[x+2][y] = "#"    #16
            playBoard[x+2][y-1] = "#"  #17
            return playBoard
        #18,19
        elif(visitedSci[18] != False and visitedSci[19] != False):
            playBoard[x][y] = "#"      #0
            playBoard[x+1][y] = "#"    #5
            playBoard[x+1][y-1]= "#"   #6
            playBoard[x][y-1] = "#"    #7
            playBoard[x+1][y-2] = "#"  #18
            playBoard[x][y-2] = "#"    #19
            return playBoard
    #0,7,8,1,
    if(visitedSci[7] != False and visitedSci[8] != False and visitedSci[1] != False):
        #19,20
        if(visitedSci[19] != False and visitedSci[20] != False):
            playBoard[x][y]= "#"       #0
            playBoard[x-1][y]= "#"     #7
            playBoard[x-1][y-1]= "#"   #8
            playBoard[x][y-1]= "#"     #1
            playBoard[x][y-2] = "#"    #19
            playBoard[x-1][y-2] = "#"  #20
            return playBoard
        
        #9,10
        elif(visitedSci[9] != False and visitedSci[10] != False):
            playBoard[x][y]= "#"       #0
            playBoard[x-1][y]= "#"     #7
            playBoard[x-1][y-1]= "#"   #8
            playBoard[x][y-1]= "#"     #1
            playBoard[x-2][y-1] = "#"  #9
            playBoard[x-2][y] = "#"    #10
            return playBoard
    
    return -1

if(testVar == 1):
    printBoard(ALLBOARDS[0])
    print("@@@@@@@@@@@@@@@@@@@\n")
    testA = ALLBOARDS[0]
    testA = makeSci(0,0,testA)
    if testA == -1:
        print("Failed")
    else:
        #print(testB)
        printBoard(testA)


#indexes in the visited array around the vertex
#Creates a used array of all visited points around the vertex than allows us to creates the object based off of it
#Figure 2 Present Search Area
#8  1  2 
#7  0  3
#6  5  4

#legend:
#same as scissors, the numbers above each if statement tell which statement it is checking for with in the above figure
def makePres(x,y,playBoard):
    visitedPr = [False for i in range(9)]
    vertex = playBoard[x][y]
    if vertex in nonos:
        return -1
    else:
        visitedPr[0] = True
        
    #for loop to fill the vis array 
    for i in range(len(CORDSROWPRES)):
        if ((x + CORDSROWPRES[i]) > boardDim or (x + CORDSROWPRES[i]) < 0):
            visitedPr[i] = False
        elif ((y + CORDSCOLPRES[i]) > boardDim or (y + CORDSCOLPRES[i]) < 0):
            visitedPr[i] = False
        else:
            vertex = playBoard[x+CORDSROWPRES[i]][y + CORDSCOLPRES[i]]
            if vertex in nonos:
                visitedPr[i] = False
            else:
                visitedPr[i] = True
    
    if(visitedPr[1] != False and visitedPr[2] != False and visitedPr[3] !=False):
        playBoard[x][y] = "!"      #0
        playBoard[x-1][y] = "!"    #1
        playBoard[x-1][y+1]= "!"   #2
        playBoard[x][y+1]= "!"     #3
        return playBoard
    elif(visitedPr[3] != False and visitedPr[4] != False and visitedPr[5] !=False):
        playBoard[x][y]= "!"       #0
        playBoard[x][y+1]= "!"     #3
        playBoard[x+1][y+1]= "!"   #4
        playBoard[x+1][y]= "!"     #5 
        return playBoard
    elif(visitedPr[5] != False and visitedPr[6] != False and visitedPr[7] !=False):
        playBoard[x][y] = "!"      #0
        playBoard[x+1][y] = "!"    #5
        playBoard[x+1][y-1]= "!"   #6
        playBoard[x][y-1] = "!"    #7
        return playBoard
    elif(visitedPr[7] != False and visitedPr[8] != False and visitedPr[1] !=False):
        playBoard[x][y]= "!"       #0
        playBoard[x-1][y]= "!"     #7
        playBoard[x-1][y-1]= "!"   #8
        playBoard[x][y-1]= "!"     #1
        return playBoard
    else:
        return -1

if(testVar == 1):
    print("@@@@@@@@@@@@@@@@@@@\n")
    printBoard(ALLBOARDS[0])
    testB = ALLBOARDS[0]
    testB = makePres(3,3,testB)
    if testB == -1:
            print("Failed")
    else:
        #print(testB)
        printBoard(testB)






def boundsFaux(x,y,playBoard):
    vertex = playBoard[x][y]
    if vertex in nonos:
        return -1
    

def faux(playBoard, ind_x, ind_y):
    newboard = playBoard
    
    if boundsFaux(ind_x, ind_y, newboard) == -1:
        return -1
    else:
        newboard[ind_x][ind_y] = "*"
        return newboard
        



def generateboard():
    iBoardD = boardDim-1
    
    ind_x = random.randrange(0,iBoardD)
    ind_y = random.randrange(0,iBoardD)
    #print(ind_x, ind_y)
    
    #random var for board number
    num = random.randrange(0,1)
    #this chosenBoard var will be changed as the board is generated
    #done to save the original chosen boards state in the ALLBOARDS list
    chosenBoard = deepcopy(ALLBOARDS[num])
    playBoard = deepcopy(ALLBOARDS[num])
    baseBoard = deepcopy(ALLBOARDS[num])
    #printBoard(playBoard)
    # k == size of the box, not needed anymore, relic of older functions
    #k = 2
    scissorsVar = makeSci( ind_x, ind_y,playBoard)
    
    #iter checks to see if the board is correct
    iter = 0

    while iter == 0:
        #-1 = vertex is not able to be placed
        if type(scissorsVar) != list :

            ind_x = random.randrange(0,iBoardD)
            ind_y = random.randrange(0,iBoardD)
            #print(ind_x, ind_y)
            
            #empty visited arr for next iter
            
            playBoard = deepcopy(chosenBoard)
            scissorsVar = makeSci( ind_x, ind_y,playBoard)
        else:
            iter = 1

    #reset iter
    iter = 0
    #playboard and chosenBoard is now equal to the board with scissors in it
    playBoard = scissorsVar
    chosenBoard = scissorsVar
    if (testVar == 1):
        printBoard(playBoard)
    #creating random index for present
    ind_x = random.randrange(0,iBoardD)
    ind_y = random.randrange(0,iBoardD)
    
    squareVar = makePres(ind_x, ind_y,playBoard)
    while iter == 0:
        #-1 = vertex is equal to @
        if type(squareVar) != list :
            
            ind_x = random.randrange(0,iBoardD)
            ind_y = random.randrange(0,iBoardD)
            #print(ind_x, ind_y)

            
            playBoard = deepcopy(chosenBoard)
            squareVar = makePres(ind_x, ind_y,playBoard)
        else:
            iter = 1
    #playBoard and chosen baord set equal to the correct squareVar with present and scissors
    playBoard = squareVar
    chosenBoard = squareVar
    
    #reset iter one last time
    iter = 0
    #generate random index for the faux
    f_x = random.randrange(0,5)
    f_y = random.randrange(0,5)
    
    #some format of the xxxVar to deliintate which iteration we are on and check if it correct and doable
    fauxVar = faux(playBoard, f_x, f_y)
    
    while iter == 0:
        if type(fauxVar) != list:
            f_x = random.randrange(0,iBoardD)
            f_y = random.randrange(0,iBoardD)
        
            
            playBoard = deepcopy(chosenBoard)
            fauxVar = faux(playBoard, f_x, f_y)
        else:
            iter = 1
    #set the board the payer will be using to the one with all elements within it
    playBoard = fauxVar
    
    #test

    
    #key is index 0, the base boards is index 1
    #so much typing of the word board...
    
    
    boards = [playBoard, ALLBOARDS[num]]
    
    return boards


'''
if testVar == 1:
    newBoard = []
    newBoard = generateboard()

    print(newBoard)

    if(type(newBoard[0]) is int):
        print(newBoard[0])
    else:
        printBoard(newBoard[0])
    print("@@@@@@@@@@@@@@@@@\n")
    printBoard(newBoard[1])
    
'''
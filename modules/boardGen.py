import random
import time

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
#['X','@','X','X','X','X']


#Now start the present case than actually taking inoput from user
# todo:
#Finish BFS and try ang et it to work, if not, if statements it is:(
#if bfs is do able, fix the gen board function than test test test
#x and y are swapped but its too far in to fix this :(




boardDim = 6
board1 = [['X','X','X','X','X','X'],['X','X','@','X','X','X'],['X','X','X','X','@','X'],['X','X','X','X','X','@'],['X','@','X','X','X','X'],['X','X','X','@','X','X']]
board2 = [['X','X','@','X','X','X'],['X','X','X','X','@','X'],['X','X','X','X','X','X'],['X','X','X','X','X','X'],['X','X','X','X','@','X'],['X','@','X','X','X','X']]
allBoards = [board1, board2]
#list of what you dont want to overwrite
nonos = ['@', '#', '!']

#dfs cords for scissors
cordsRowS = [0,1,0,-1,0,2,0,-2]
cordsColS = [-1,0,1,0,-2,0,2]

#dfs coords for present
cordsRowP = [0,1,0,-1]
cordsColP = [-1,0,1,0]

#shouldnt be used outside of testing this specific py file
def printBoard(playBoard):
    for count, ele in enumerate(playBoard):
        print(count, ele)

#this should really be rewritten       
def bounds(x, y, playBoard, type):
    #the type var tells whether it is 0, for rectangle (scissors) or 1 for a square (present)

    #tells eiterh scissors or present or even faux selector where it can build, either left or right, up or down
    #possibly could return a list first val being wther it can go left or right and 2nd val being whethere up or down
    #returns -1 if it is a failed vertex, 0 if it is a build right2 down1 and 1 if it is a build right2 up1 case, 2 if it is build left2 and down1 and 3 if build left2 and up1, 
    #returns 4 if build right1 down2, 5 if build right1 up3, 6 if build left1 down3, 7 if build left1 up3
    vertex = playBoard[x][y]
    if vertex in nonos:
        print("0")
        print(vertex)
        return -1
    #cases where x is on far right and we are building to horizontally 3x2
    if (x + 1) < 6 and playBoard[x+1][y] not in nonos:
        #x is on the far right
        if type == 0 and (y + 2) < 6 and playBoard[x][y+1] not in nonos and playBoard[x][y+2] not in nonos and playBoard[x+1][y+1] not in nonos and playBoard[x+1][y+2] not in nonos :
            #building to the right down from the top left corner a 3x2 rectangle
            return 0
        elif type == 0 and (y - 2) >= 0 and playBoard[x][y-1] not in nonos and playBoard[x][y-2] not in nonos and playBoard[x+1][y-1] not in nonos and playBoard[x+1][y-2] not in nonos :
            #building to the right up from the top left corner a 3x2 rectangle
            return 1
            
        #now for the square checks
        if type == 1 and (y + 1) < 6 and playBoard[x][y+1] not in nonos and playBoard[x+1][y+1] not in nonos :
            #building to the right down from the top left corner a 3x2 rectangle
            return 0
        elif type == 1 and (y - 1) >= 0 and playBoard[x][y-1] not in nonos and playBoard[x+1][y-1] not in nonos:
            #building to the right up from the top left corner a 3x2 rectangle
            return 1

    if (x-1) >= 0 and playBoard[x-1][y] not in nonos :
        #case where x is on far left
        if type == 0 and (y + 2) < 6 and playBoard[x][y+1] not in nonos and playBoard[x][y+2] not in nonos and playBoard[x-1][y+1] not in nonos and playBoard[x-1][y+2] not in nonos :
            #building up and to the right a 3x2 rectangle or 2x2 square
            return 2
        elif type == 0 and (y - 2) >= 0 and playBoard[x][y-1] not in nonos and playBoard[x][y-2] not in nonos and playBoard[x-1][y-1] not in nonos and playBoard[x-1][y-2] not in nonos :
            #building down and to the left a 3x2 rectangle
            return 3
        
        #now for the square checks
        if type == 1 and (y + 1) < 6 and playBoard[x][y+1] not in nonos and playBoard[x-1][y+1] not in nonos :
            #building up and to the right a 3x2 rectangle or 2x2 square
            return 2
        elif type == 1 and (y - 1) >= 0 and playBoard[x][y-1] not in nonos and playBoard[x-1][y-1] not in nonos:
            #building down and to the left a 3x2 rectangle
            return 3

    #case where x is on far right and we are building down 2x3
    if type == 0 and (x+2) < 6 and playBoard[x+2][y] not in nonos  and playBoard[x+1][y] not in nonos :
        if playBoard[x+2][y] not in nonos  and playBoard[x+2][y+1] not in nonos  and playBoard[x+1][y+1] not in nonos  and playBoard[x][y+1] not in nonos :
            #building to the right and down from the top left corner a 2x3 rectangle
            return 4
        elif playBoard[x+2][y] not in nonos  and playBoard[x+2][y-1] not in nonos  and playBoard[x+1][y-1] !='@'and playBoard[x][y-1] not in nonos :
            #building to the right and up from the top left corner a 2x3 rectangle
            return 5
    if type == 0 and (x-2) >=0 and playBoard[x-2][y] not in nonos and playBoard[x+1][y] not in nonos :
        if playBoard[x-2][y+1] not in nonos  and playBoard[x-1][y+1] not in nonos and playBoard[x][y+1] not in nonos :
            #building down and to the left  corner a 2x3 rectanlge
            return 6
        elif playBoard[x-2][y-1] not in nonos  and playBoard[x-2][y-1] not in nonos  and playBoard[x][y-1] not in nonos :
            #building up and to the left  corner a 2x3 rectanlge
            return 7
    else:
        return -1

vis = [[False for i in range(boardDim)] for j in range(boardDim)]

def isValid(row, col, playBoard):
    #out of bounds
    if(row < 0 or col < 0 or row > boardDim or col > boardDim):
        return False
    
    #already visited
    if(vis[row][col]):
        return False
    #is occupied by an invalid char
    if(playBoard[row][col] in nonos):
        return False
    
    return True


#the type var tells whether it is 0 for rectangle (scissors) or 1 for a square (present)
def dfs(x, y, playBoard, type):
    st = [x, y]
    
    
    if type == 0:

        
        
    elif type == 1:
        while len()
        

    else:
        return -1

def boundsScissors(x, y, playBoard):
    vertex = playBoard[x][y]
    if vertex in nonos:
        print("0")
        print(vertex)
        return -1
    
    #IMPORTANT
    #these next if statements (the bulk of this function) will follow a similar structure of checking first if the x than y (+- 1 or 2 for x than y)are out of bounds than checking if they are invalid characters to place over 
    
    #checking is building "down" and to the "right" is possible vertically meaning x will have the +2
    #vertical Copy point
    if (x+2) <= boardDim and (y+1) <=boardDim and playBoard[x][y] != "@" and playBoard[x+1][y] != "@" and playBoard[x+2][y] != "@" and playBoard[x][y+1] != "@" and playBoard[x+1][y+1] != "@" and playBoard[x+2][y+1] != "@":
        playBoard[x][y] = "#"
        playBoard[x+1][y] = "#"
        playBoard[x+2][y] = "#"
        playBoard[x][y+1] = "#"
        playBoard[x+1][y+1] = "#"
        playBoard[x+2][y+1] = "#"
        return playBoard
    #horizontal copy point
    #checking is building "down" and to the "right" is possible horizontally meaning y will have the +2
    elif (x+1) <= boardDim and (y+2) <=boardDim and playBoard[x][y] != "@" and playBoard[x+1][y] != "@" and playBoard[x][y+1] != "@" and playBoard[x+1][y+1] != "@" and playBoard[x][y+2] != "@" and playBoard[x+1][y+2] != "@":
        playBoard[x][y] = "#"
        playBoard[x+1][y] = "#"
        playBoard[x][y+1] = "#"
        playBoard[x][y+2] = "#"
        playBoard[x+1][y+1] = "#"
        playBoard[x+1][y+2] = "#"
        return playBoard
    
    #checking if building down and to the "left" is possible vertically
    elif (x+1) <= boardDim and (y-1) >0 and playBoard[x+1][y] not in nonos and playBoard[x][y-1] not in nonos and playBoard[x+1][y-1] not in nonos:
        playBoard[x][y] = "!"
        playBoard[x+1][y] = "!"
        playBoard[x][y-1] = "!"
        playBoard[x+1][y-1] = "!"
        return playBoard
    #checking if building "up" and to the "right" is possible
    elif(x-1) >0 and (y+1) <=boardDim and playBoard[x-1][y] not in nonos and playBoard[x][y+1] not in nonos and playBoard[x-1][y+1] not in nonos:
        playBoard[x][y] = "!"
        playBoard[x-1][y] = "!"
        playBoard[x][y+1] = "!"
        playBoard[x-1][y+1] = "!"
        return playBoard
    #checking is building "up" and to the "left" is possible
    elif(x-1) >0 and (y-1) >0 and playBoard[x-1][y] not in nonos and playBoard[x][y-1] not in nonos and playBoard[x-1][y-1] not in nonos:
        playBoard[x][y] = "!"
        playBoard[x-1][y] = "!"
        playBoard[x][y-1] = "!"
        playBoard[x-1][y-1] = "!"
        return playBoard
    else:
        return -1

def boundsPresent(x,y,playBoard):
    vertex = playBoard[x][y]
    if vertex in nonos:
        print("0")
        print(vertex)
        return -1
    
    #IMPORTANT
    #these next if statements (the bulk of this function) will follow a similar structure of checking first if the x than y are out of bounds than checking if they are invalid characters to place over
    
    #checking is building "down" and to the "right" is possible
    if (x+1) <= boardDim and (y+1) <=boardDim and playBoard[x+1][y] not in nonos and playBoard[x][y+1] not in nonos and playBoard[x+1][y+1] not in nonos:
        playBoard[x][y] = "!"
        playBoard[x+1][y] = "!"
        playBoard[x][y+1] = "!"
        playBoard[x+1][y+1] = "!"
        return playBoard
    #checking if building down and to the "left" is possible
    elif (x+1) <= boardDim and (y-1) >0 and playBoard[x+1][y] not in nonos and playBoard[x][y-1] not in nonos and playBoard[x+1][y-1] not in nonos:
        playBoard[x][y] = "!"
        playBoard[x+1][y] = "!"
        playBoard[x][y-1] = "!"
        playBoard[x+1][y-1] = "!"
        return playBoard
    #checking if building "up" and to the "right" is possible
    elif(x-1) >0 and (y+1) <=boardDim and playBoard[x-1][y] not in nonos and playBoard[x][y+1] not in nonos and playBoard[x-1][y+1] not in nonos:
        playBoard[x][y] = "!"
        playBoard[x-1][y] = "!"
        playBoard[x][y+1] = "!"
        playBoard[x-1][y+1] = "!"
        return playBoard
    #checking is building "up" and to the "left" is possible
    elif(x-1) >0 and (y-1) >0 and playBoard[x-1][y] not in nonos and playBoard[x][y-1] not in nonos and playBoard[x-1][y-1] not in nonos:
        playBoard[x][y] = "!"
        playBoard[x-1][y] = "!"
        playBoard[x][y-1] = "!"
        playBoard[x-1][y-1] = "!"
        return playBoard
    else:
        return -1
    


def boundsFaux(x,y,playBoard):
    vertex = playBoard[x][y]
    if vertex in nonos:
        print("0")
        print(vertex)
        return -1
    
        


def scissors(playBoard, ind_x, ind_y, k):
    newboard = playBoard
    fail = -1

    #x coord of position for scissors
    row = playBoard[ind_x]
    #y coord of position for scissors
    col = row[ind_y]
    vertex = playBoard[ind_x][ind_y]
    #print(bounds(ind_x, ind_y, newboard, 0))
    if k >= 0:
        #if starting point vertex is a unplaceable or if 
        if bounds(ind_x, ind_y, newboard, 0) < 0:
            #print("0")
            #print(vertex)
            return fail
        #i hate this, surely the 2x2 will look nicer 
        bounds(ind_x, ind_y, newboard, 0)
        match(bounds(ind_x, ind_y, newboard, 0)):
            #horizontal fill 
            case 0:
                newboard[ind_x][ind_y] = '#'
                newboard[ind_x][ind_y+1] = '#'
                newboard[ind_x][ind_y+2] = '#'
                newboard[ind_x+1][ind_y] = '#'
                newboard[ind_x+1][ind_y+1] = '#'
                newboard[ind_x+1][ind_y+2] = '#'
            case 1:
                newboard[ind_x][ind_y] = '#'
                newboard[ind_x][ind_y-1] = '#'
                newboard[ind_x][ind_y-2] = '#'
                newboard[ind_x+1][ind_y] = '#'
                newboard[ind_x+1][ind_y-1] = '#'
                newboard[ind_x+1][ind_y-2] = '#'
            case 2:
                newboard[ind_x][ind_y] = '#'
                newboard[ind_x][ind_y+1] = '#'
                newboard[ind_x][ind_y+2] = '#'
                newboard[ind_x-1][ind_y] = '#'
                newboard[ind_x-1][ind_y+1] = '#'
                newboard[ind_x-1][ind_y+2] = '#'
            case 3:
                newboard[ind_x][ind_y] = '#'
                newboard[ind_x][ind_y-1] = '#'
                newboard[ind_x][ind_y-2] = '#'
                newboard[ind_x-1][ind_y] = '#'
                newboard[ind_x-1][ind_y-1] = '#'
                newboard[ind_x-1][ind_y-2] = '#'
            #now begin the vertical fill
            case 4:
                newboard[ind_x][ind_y] = '#'
                newboard[ind_x+1][ind_y] = '#'
                newboard[ind_x+2][ind_y] = '#'
                newboard[ind_x][ind_y+1] = '#'
                newboard[ind_x+1][ind_y+1] = '#'
                newboard[ind_x+2][ind_y+1] = '#'
            case 5:
                newboard[ind_x][ind_y] = '#'
                newboard[ind_x+1][ind_y] = '#'
                newboard[ind_x+2][ind_y] = '#'
                newboard[ind_x][ind_y-1] = '#'
                newboard[ind_x+1][ind_y-1] = '#'
                newboard[ind_x+2][ind_y-1] = '#'
            case 6:
                newboard[ind_x][ind_y] = '#'
                newboard[ind_x-1][ind_y] = '#'
                newboard[ind_x-2][ind_y] = '#'
                newboard[ind_x][ind_y+1] = '#'
                newboard[ind_x-1][ind_y+1] = '#'
                newboard[ind_x-2][ind_y+1] = '#'
            case 7:
                newboard[ind_x][ind_y] = '#'
                newboard[ind_x-1][ind_y] = '#'
                newboard[ind_x-2][ind_y] = '#'
                newboard[ind_x][ind_y-1] = '#'
                newboard[ind_x-1][ind_y-1] = '#'
                newboard[ind_x-2][ind_y-1] = '#'
            case _:
                #print("0")
                #print(vertex)
                return fail
    return newboard

'''
This function is defunct by the boundsPresent function, probably for the better

def presentBox(playBoard, ind_x, ind_y, k):
    newboard = playBoard
    fail = -1

    #x coord of position for scissors
    row = playBoard[ind_x]
    #y coord of position for scissors
    col = row[ind_y]
    vertex = playBoard[ind_x][ind_y]
    #print(bounds(ind_x, ind_y, newboard))
    if k >= 0:
        #if starting point vertex is a unplaceable or if 
        if bounds(ind_x, ind_y, newboard,1) < 0:
            #print("0")
            #print(vertex)
            return fail
        
        bounds(ind_x, ind_y, newboard,1)
        match(bounds(ind_x, ind_y, newboard,1)):
            #horizontal fill 
            case 0:
                newboard[ind_x][ind_y] = '!'
                newboard[ind_x][ind_y+1] = '!'
                newboard[ind_x+1][ind_y] = '!'
                newboard[ind_x+1][ind_y+1] = '!'
            case 1:
                newboard[ind_x][ind_y] = '!'
                newboard[ind_x][ind_y-1] = '!'
                newboard[ind_x+1][ind_y] = '!'
                newboard[ind_x+1][ind_y-1] = '!'
            case 2:
                newboard[ind_x][ind_y] = '!'
                newboard[ind_x][ind_y+1] = '!'
                newboard[ind_x-1][ind_y] = '!'
                newboard[ind_x-1][ind_y+1] = '!'
            case 3:
                newboard[ind_x][ind_y] = '!'
                newboard[ind_x][ind_y-1] = '!'
                newboard[ind_x-1][ind_y] = '!'
                newboard[ind_x-1][ind_y-1] = '!'
            case _:
                #print("0")
                #print(vertex)
                return fail
    return newboard

'''

def faux(playBoard, ind_x, ind_y, k):
    fail = -1
    newboard = playBoard
    
    if k>=0:
        if boundsFaux(ind_x, ind_y, newboard,1) == -1:
            #print("0")
            #print(vertex)
            return fail
        else:
            newboard[ind_x][ind_y] = "*"
            return newboard
        

def generateboard():
    ind_x = random.randrange(0,5)
    ind_y = random.randrange(0,5)
    #print(ind_x, ind_y)
    num = random.randrange(0,1)
    #this chosenBoard var will be changed as the board is generated
    #done to save the original chosen boards state in the allBoards list
    chosenBoard = allBoards[num]
    playBoard = chosenBoard
    #printBoard(playBoard)
    # k == size of the box
    k = 2
    scissorsVar = scissors(playBoard, ind_x, ind_y, k)
    
    #iter checks to see if the board is correct
    iter = 0
    while iter == 0:
        #-1 = vertex is equal to @
        if scissorsVar == -1:
            ind_x = random.randrange(0,5)
            ind_y = random.randrange(0,5)
            #print(ind_x, ind_y)
            vis = [[False for i in range(boardDim)] for j in range(boardDim)]
            
            playBoard = chosenBoard
            scissorsVar = scissors(playBoard, ind_x, ind_y, k)
        else:
            iter = 1
    #reset iter and visited for the square
    vis = [[False for i in range(boardDim)] for j in range(boardDim)]
    iter = 0
    #playboard is now equal to the 
    playBoard = scissorsVar
    printBoard(playBoard)
    ind_x = random.randrange(0,5)
    ind_y = random.randrange(0,5)
    squareVar = boundsPresent(playBoard, ind_x, ind_y,k)
    while iter == 0:
        #-1 = vertex is equal to @
        if squareVar == -1:
            ind_x = random.randrange(0,5)
            ind_y = random.randrange(0,5)
            #print(ind_x, ind_y)
            vis = [[False for i in range(boardDim)] for j in range(boardDim)]
            
            playBoard = chosenBoard
            squareVar = boundsPresent(playBoard, ind_x, ind_y, k)
        else:
            iter = 1
    #boardTest = allBoards[0]
    #print(bounds(0, 0, boardTest), "HELP")
    
    #reset iter and vis one last time
    vis = [[False for i in range(boardDim)] for j in range(boardDim)]
    iter = 0
    #generate random index for the faux
    f_x = random.randrange(0,5)
    f_y = random.randrange(0,5)
    #some format of the xxxVar to deliintate which iteration we are on and check if it correct and doable
    fauxVar = faux(playBoard, f_x, f_y, k)
    while iter == 0:
        if fauxVar == -1:
            f_x = random.randrange(0,5)
            f_y = random.randrange(0,5)
            
            vis = [[False for i in range(boardDim)] for j in range(boardDim)]
            
            playBoard = chosenBoard
            fauxVar = faux(playBoard, f_x, f_y, k)
        else:
            iter = 1
    #set the board the payer will be using to the one with all elements within it
    playBoard = fauxVar
    
    #test
    printBoard(playBoard)
    
    #key is index 0, the base boards is index 1
    #so much typing of the word board...
    boards = [playBoard, allBoards[num]]
    
    return boards
    

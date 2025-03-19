import random
import time
from modules import boardGen
from modules import extraCCC



# # == to scissors, @ == unplaceable, ! == to present, X == placeable, * == faux


def main():

    #key is index 0, the base boards is index 1
    keyAndVal = boardGen.generateboard()
    key = keyAndVal[0]
    baseBoard = keyAndVal[1]
    
    # user gets 7 tries of different coordinates
    
    baseBoard = extraCCC.wrapBoard(baseBoard)
    
    #extraCCC.beginGame()
        
    


if __name__ == "main":
    main()

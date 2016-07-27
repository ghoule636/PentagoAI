"""
# Gabriel Houle
# Programming Assignment 2
# TCSS 435 AI Spring 2016
"""

import sys
from Board import Board

global player1Name
global player2Name
global player1Color
global player2Color
global isAI

def main() :
    global player1Name
    global player2Name
    global player1Color
    global player2Color
    global isAI

    testBoard()  #This function is used for testing board functionality.

    #start(initializeGame())

def initializeGame() :
    import random
    global player1Name
    global player2Name
    global player1Color
    global player2Color
    global isAI

    player1Name = input("Player 1 Name: ")
    player2Name = input("Player 2 Name: ")
    player1Color = ""

    while (player1Color != 'w' and player1Color != 'b') :
        player1Color = input("Player 1 Token Color (B or W): ")
        if (player1Color.lower() == 'w') :
            player1Color = 'w'
            player2Color = 'b'
        elif (player1Color.lower() == 'b') :
            player1Color = 'b'
            player2Color = 'w'
        else :
            print("Invalid color choice! Choose B or W")

    if (player1Color == 'w') :
        colorChoice = "White"
    elif (player1Color == 'b') :
        colorChoice = "Black"

    isAI = ''
    while (isAI != 'y' and isAI != 'n') :

        isAI = input("Is player 2 a computer? y/n?: ")
        if (isAI.lower() == 'y') :
            isAI = 'y'
        elif (isAI.lower() == 'n') :
            isAI = 'n'
        else :
            print("Invalid Choice type Y or N")


    print("Welcome {0}!".format(player1Name), end='')
    print(" You have chosen: {0}".format(colorChoice))
    random.seed()
    goFirst = random.randint(1, 2)

    print("Player {0} goes first".format(goFirst))

    return goFirst

def start(firstMove) :

    board = Board()

    print("\n\nInitial State:\n")
    print(board)

    

    return 0

def humanMove() :
    return 0

def testBoard() :
    test = Board()

    print(test)

    #test.addPiece(3, 3, "w")
    """
    # horizontal win config
    test.addPiece(3, 7, 'b')
    test.addPiece(3, 8, 'b')
    test.addPiece(3, 9, 'b')
    test.addPiece(4, 7, 'b')
    test.addPiece(4, 8, 'b')

    # horizontal config 2
    test.addPiece(1, 1, 'w')
    test.addPiece(1, 2, 'w')
    test.addPiece(1, 3, 'w')
    test.addPiece(2, 1, 'w')
    test.addPiece(2, 2, 'w')
    test.addPiece(2, 3, 'b')
    """

    # vertical win config
    """
    test.addPiece(2, 3, 'w')
    test.addPiece(2, 6, 'w')
    test.addPiece(2, 9, 'w')
    test.addPiece(4, 3, 'w')
    test.addPiece(4, 6, 'w')
    test.addPiece(4, 9, 'b')

    # vertical config 2
    test.addPiece(1, 1, 'b')
    test.addPiece(1, 4, 'b')
    test.addPiece(1, 7, 'b')
    test.addPiece(3, 1, 'b')
    test.addPiece(3, 4, 'b')
    #test.addPiece(3, 7, 'w')
    """    

    # diagonal win config
    test.addPiece(1, 1, 'w')

    print("win? : {0}".format(test.checkWin()))

    print(test)

main()
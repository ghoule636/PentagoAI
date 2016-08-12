"""
# Gabriel Houle
# Programming Assignment 2
# TCSS 435 AI Spring 2016
"""

import sys
from Board import Board
import AI
import random

global player1Name
global player2Name
global player1Color
global player2Color
global isAI
global moveList
global outputFile
global maxDepth

def main() :
    global player1Name
    global player2Name
    global player1Color
    global player2Color
    global isAI
    global moveList
    global maxDepth
    global outputFile

    outputFile = open("output.txt", 'w')
    maxDepth = 3

    #testBoard()  #This function is used for testing board functionality.

    testAI() # This is used to test the AI functionality.

    #start(initializeGame()) # This function starts the main game.

def initializeGame() :
    global player1Name
    global player2Name
    global player1Color
    global player2Color
    global isAI
    global moveList
    global outputFile

    moveList = []
        
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
    outputFile.write("Player 1 Name: {0}\nPlayer 2 Name: {1}\nPlayer 1 Color: {2}\nPlayer 2 Color: {3}\n".format(player1Name, player2Name, player1Color, player2Color))
    random.seed()
    goFirst = random.randint(1, 2)

    print("Player {0} goes first".format(goFirst))

    return goFirst

def start(firstMove) :
    global player1Name
    global player2Name
    global player1Color
    global player2Color
    global isAI
    global outputFile

    board = Board()

    print("\n\nInitial State:\n")
    print(board)

    winner = board.checkWin()
    while (winner == -1) :
        if (firstMove == 1) :
            print("{0}'s turn".format(player1Name))
            humanMove(board, player1Color)
            print(board)
            winner = board.checkWin()
            if (winner == -1) :
                print("{0}'s turn".format(player2Name))
                if (isAI == 'y') :
                    print("Computer Turn")
                    AIMove(board, player2Color)
                    print(board)
                elif (winner == -1) :
                    humanMove(board, player2Color)
                    print(board)
        else :
            print("{0}'s turn".format(player2Name))
            if (isAI == 'y') :
                print("Computer Turn")
                AIMove(board, player2Color)
                print(board)
            else :
                humanMove(board, player2Color)
                print(board)
            winner == board.checkWin()
            if (winner == -1) :
                print("{0}'s turn".format(player1Name))
                humanMove(board, player1Color)
                print(board)

        winner = board.checkWin()
    print("Game Over!")
    if (winner == 0) :
        winNum = -1
        if (player1Color == 'w') :
            winNum = 0
        else :
            winNum = 1
    elif (winner == 1) :
        if (player1Color == 'b') :
            winNum = 0
        else :
            winNum = 1
    elif (winner == 2) :
        winNum = -1
        print("\nTie!\n")

    if (winNum == 0) :
        print("\nCongratulations {0}, You Win!\n".format(player1Name))
    elif (winNum == 1) :
        print ("\nCongratulations {0}, You Win!\n".format(player2Name))


    return 0

def AIMove(board, type) :
    global maxDepth

    move = AI.decideMove(board, maxDepth)

    print("AI move: " + str(move))


def humanMove(board, type) :
    global moveList
    global outputFile

    move = input("Move: ")

    boardNum = int(move[0])
    pos = int(move[2])
    boardRotate = move[4]
    rotateDir = move[5]

    check = board.addPiece(boardNum, pos, type)

    while (not check) :
        move = input("Invalid move try again")
        boardNum = int(move[0])
        pos = int(move[2])
        boardRotate = move[4]
        rotateDir = move[5]

        check = board.addPiece(boardNum, pos, type)
        
    winCheck = board.checkWin()
    if (winCheck == -1) :
        if (rotateDir.lower() == 'l') :
            board.shiftLeft(int(boardRotate))
        else :
            board.shiftRight(int(boardRotate))
    moveList.append(move)
    outputFile.write(str(board) + "\n")
    outputFile.write(str(moveList) + "\n")

def testBoard() :
    test = Board()

    print(test)
    
    # horizontal win config
    """
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

    # diagonal win configs
    """
    test.addPiece(1, 1, 'w')
    test.addPiece(1, 5, 'b')
    test.addPiece(1, 9, 'b')
    test.addPiece(4, 1, 'b')
    test.addPiece(4, 5, 'b')
    test.addPiece(4, 9, 'b')

    test.addPiece(2, 3, 'w')
    test.addPiece(2, 5, 'w')
    test.addPiece(2, 7, 'w')
    test.addPiece(3, 3, 'w')
    test.addPiece(3, 5, 'w')
    test.addPiece(3, 7, 'b')
    """
    
    test.addPiece(1, 2, 'w')
    test.addPiece(1, 6, 'w')
    test.addPiece(2, 7, 'w')
    test.addPiece(4, 2, 'w')
    test.addPiece(4, 6, 'w')
    
    test.addPiece(1, 4, 'b')
    test.addPiece(1, 8, 'b')
    test.addPiece(3, 3, 'b')
    test.addPiece(4, 4, 'b')
    test.addPiece(4, 8, 'b')
    
    test.addPiece(2, 2, 'w')
    test.addPiece(2, 4, 'w')
    test.addPiece(1, 9, 'w')
    test.addPiece(3, 2, 'w')
    test.addPiece(3, 4, 'b')

    test.addPiece(2, 6, 'b')
    test.addPiece(2, 8, 'b')
    test.addPiece(4, 1, 'b')
    test.addPiece(3, 6, 'b')
    test.addPiece(3, 8, 'b')
    
    print("win? : {0}".format(test.checkWin()))

    print(test)

def testAI() :
    test = Board()
    maxDepth = 2

    test.addPiece(3, 7, 'b')
    test.addPiece(3, 8, 'b')
    test.addPiece(3, 9, 'b')
    test.addPiece(4, 7, 'b')
    test.addPiece(4, 8, 'b')

    test2 = test.copyBoard()

    test2.addPiece(1, 1, 'w')
    print(test)
    #print(test2)

    AI.decideMove(test, maxDepth)

main()
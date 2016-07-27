"""
# Gabriel Houle
# Programming Assignment 2
# TCSS 435 AI Spring 2016
"""

class Board:
    def __init__(self) :
        self.__board = [0] * 4
        self.__board[0] = ['.'] * 9
        self.__board[1] = ['.'] * 9
        self.__board[2] = ['.'] * 9
        self.__board[3] = ['.'] * 9

    # Adds type char to selected block and position.
    # Will return false if this position is already taken or
    # if the block or position is invalid.
    def addPiece(self, block, pos, type) :
        result = True
        pos = pos - 1
        if (pos > 8 or pos < 0) :
            result = False
        if (block < 1 or block > 4) :
            result = False
        if (result) :
            if(self.__board[block - 1][pos] == '.') :
                self.__board[block - 1][pos] = type
            else :
                result = False

        return result

    # Shift selected board right
    def shiftRight(boardNum) :
        return False

    # Shift selected board left
    def shiftLeft(boardNum) :
        return False

    #Returns -1 if no winner, 0 if w is winner, 1 if b is winner, 2 or greater if tie
    def checkWin(self) :
        import math
        result = -1
        blackWin = False
        whiteWin = False

        charCheck = ''
        charCount = 0

        i = 0
        j = 0
        k = 0

        # vertical checks
        while (i < 6) :
            while (j <= 3) :
                while (k < 3) :
                    if (self.__board[j + math.floor(i / 3)][(i % 3) + (3 * k)] != '.') :
                        if (self.__board[j  + math.floor(i / 3)][(i % 3) + (3 * k)] != charCheck) :
                            charCheck = self.__board[j + math.floor(i / 3)][(i % 3) + (3 * k)]
                            charCount = 1
                        else :
                            charCount += 1
                    else :
                        charCount = 0
                        charCheck = ''
                    k += 1
                    if (charCount == 5) :
                        if (charCheck == 'b' and not blackWin) :
                            result += 2
                            blackWin = True
                        if (charCheck == 'w' and not whiteWin) :
                            result += 1
                            whiteWin = True
                j += 2
                k = 0
            charCheck = ''
            charCount = 0
            j = 0
            i += 1

        i = 0
        j = 0
        k = 0
        # horizontal checks
        while (i < 6) :
            while (j < 2) :
                while (k < 3) :
                    if (self.__board[j + (math.floor(i / 3) * 2)][((i % 3) * 3) + k] != '.') :
                        if (self.__board[j  + (math.floor(i / 3) * 2)][((i % 3) * 3) + k] != charCheck) :
                            charCheck = self.__board[j + (math.floor(i / 3) * 2)][((i % 3) * 3) + k]
                            charCount = 1
                        else :
                            charCount += 1
                    else :
                        charCount = 0
                        charCheck = ''
                    k += 1
                    if (charCount == 5) :
                        if (charCheck == 'b' and not blackWin) :
                            result += 2
                            blackWin = True
                        if (charCheck == 'w' and not whiteWin) :
                            result += 1
                            whiteWin = True
                j += 1
                k = 0  
            charCheck = ''
            charCount = 0
            j = 0
            i += 1

        i = 0
        j = 0
        k = 0
        # diagonal checks
        while (i < 4) :
            while (j < 3) :
                if (self.__board[i][j * 4] != '.') :
                    charCheck = self.__board[i][j * 4]
                    charCount += 1

                j += 1
                if (charCount == 5) :
                        if (charCheck == 'b' and not blackWin) :
                            result += 2
                            blackWin = True
                        if (charCheck == 'w' and not whiteWin) :
                            result += 1
                            whiteWin = True


            i += 2


        return result

    # Returns a String representation of the board
    def __repr__(self) :
        result = ""

        result = "+--------+--------+\n|{0}  {1}  {2} | {3}  {4}  {5}|\n|{6}  {7}  {8} | {9}  {10}  {11}|\n|{12}  {13}  {14} | {15}  {16}  {17}|\n+--------+--------+\n|{18}  {19}  {20} | {21}  {22}  {23}|\n|{24}  {25}  {26} | {27}  {28}  {29}|\n|{30}  {31}  {32} | {33}  {34}  {35}|\n+--------+--------+".format(self.__board[0][0], 
                self.__board[0][1], self.__board[0][2], self.__board[1][0], self.__board[1][1], self.__board[1][2],
                self.__board[0][3], self.__board[0][4], self.__board[0][5], self.__board[1][3], self.__board[1][4], self.__board[1][5],
                self.__board[0][6], self.__board[0][7], self.__board[0][8], self.__board[1][6], self.__board[1][7], self.__board[1][8], 
                self.__board[2][0], self.__board[2][1], self.__board[2][2], self.__board[3][0], self.__board[3][1], self.__board[3][2],
                self.__board[2][3], self.__board[2][4], self.__board[2][5], self.__board[3][3], self.__board[3][4], self.__board[3][5],
                self.__board[2][6], self.__board[2][7], self.__board[2][8], 
                self.__board[3][6],
                self.__board[3][7],
                self.__board[3][8])

        #result = str(self.__board)

        return result
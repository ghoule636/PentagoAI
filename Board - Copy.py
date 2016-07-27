"""
# Gabriel Houle
# Programming Assignment 2
# TCSS 435 AI Spring 2016
"""

class Board:
    def __init__(self) :

        self.__board1 = ['.'] * 9
        self.__board2 = ['.'] * 9
        self.__board3 = ['.'] * 9
        self.__board4 = ['.'] * 9

    # Adds type char to selected block and position.
    # Will return false if this position is already taken or
    # if the block or position is invalid.
    def addPiece(self, block, pos, type) :
        result = True
        pos = pos - 1
        if (pos > 9 or pos < 1) :
            result = False
        if (block < 1 or block > 4) :
            result = False
        if (result) :
            if (block == 1) :
                if (self.__board1[pos] == '.') :
                    self.__board1[pos] = type
                else :
                    result = False
            if (block == 2) :
                if (self.__board2[pos] == '.') :
                    self.__board2[pos] = type
                else :
                    result = False
            if (block == 3) :
                if (self.__board3[pos] == '.') :
                    self.__board3[pos] = type
                else :
                    result = False
            if (block == 4) :
                if (self.__board4[pos] == '.') :
                    self.__board4[pos] = type
                else :
                    result = False

        return result

    # Shift selected board right
    def shiftRight(boardNum) :
        return False

    # Shift selected board left
    def shiftLeft(boardNum) :
        return False

    #Returns -1 if no winner, 0 if w is winner, 1 if b is winner, 2 if tie
    def checkWin(self) :
        result = -1

        count1 = 0
        count2 = 0

        #while (count1 < 6) :
        check1 = self.__board1[0]
        check2 = self.__board1[1]
            
            
        """while (count2 < 3) :
                check = self.__board1[count2 * 3]
                count2 += 1
            count2 = 0
            while (count2 < 3) :
                check = self.__board3[count2 * 3]
                count2 += 1
            count1 += 1"""


        return result

    # Returns a String representation of the board
    def __repr__(self) :
        result = ""

        result = "+--------+--------+\n|{0}  {1}  {2} | {3}  {4}  {5}|\n|{6}  {7}  {8} | {9}  {10}  {11}|\n|{12}  {13}  {14} | {15}  {16}  {17}|\n+--------+--------+\n|{18}  {19}  {20} | {21}  {22}  {23}|\n|{24}  {25}  {26} | {27}  {28}  {29}|\n|{30}  {31}  {32} | {33}  {34}  {35}|\n+--------+--------+".format(self.__board1[0], 
                self.__board1[1], self.__board1[2], self.__board2[0], self.__board2[1], self.__board2[2],
                self.__board1[3], self.__board1[4], self.__board1[5], self.__board2[3], self.__board2[4], self.__board2[5],
                self.__board1[6], self.__board1[7], self.__board1[8], self.__board2[6], self.__board2[7], self.__board2[8], 
                self.__board3[0], self.__board3[1], self.__board3[2], self.__board4[0], self.__board4[1], self.__board4[2],
                self.__board3[3], self.__board3[4], self.__board3[5], self.__board4[3], self.__board4[4], self.__board4[5],
                self.__board3[6], self.__board3[7], self.__board3[8], 
                self.__board4[6],
                self.__board4[7],
                self.__board4[8])

        #result = str(self.__board)

        return result
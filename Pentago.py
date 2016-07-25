"""
# Gabriel Houle
# Programming Assignment 2
# TCSS 435 AI Spring 2016
"""

from Board import Board

def main() :
    test = Board()

    print(test)

    test.addPiece(3, 3, "w")
    test.addPiece(1, 5, 'b')

    print(test)

main()
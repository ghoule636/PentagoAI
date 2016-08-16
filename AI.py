"""
# Gabriel Houle
# Programming Assignment 2
# TCSS 435 AI Spring 2016
"""
from collections import deque
import sys

def decideMove(state, maxDepth, type) :
    moveTree = createTree(state, maxDepth, type)

    bestIndex = 0  
    if (type == 'w') :
        bestValue = -sys.maxsize
        for i in range(len(moveTree.children)) :
            hValue = minMax(moveTree.children[i], True, maxDepth)
            if (hValue > bestValue) :
                bestIndex = i
                bestValue = hValue

    else :
        bestValue = sys.maxsize
        for i in range(len(moveTree.children)) :
            hValue = minMax(moveTree.children[i], False, maxDepth)
            if (hValue < bestValue) :
                bestIndex = i
                bestValue = hValue

    return moveTree.children[bestIndex].move


# creates tree of moves up to maximum depth ... to consider how many moves should i consider rotations... depth 3 is 6 mill with rotations only 12000 without
def createTree(state, maxDepth, type) :
    root = Node()

    root.depth = 0
    root.data = state
    fringe = deque()

    node = root
    created = 0
    while (node.depth < maxDepth) :
        #print(created)
        for i in range(4) :
            for j in range(9) :
                pos = node.data.copyBoard()
                canMove = pos.addPiece(i + 1, j + 1, type)

                if (canMove) :
                    for k in range(4) :
                        created += 2
                        rot = pos.copyBoard()
                        rot.shiftLeft(k)

                        child = Node()
                        child.depth = node.depth + 1
                        child.data = rot
                        child.move = "{0}/{1} {2}l".format(i + 1, j + 1, k + 1)
                        node.children.append(child)
                        fringe.append(child)
                            
                        rot = pos.copyBoard()
                        rot.shiftRight(k)
                        child = Node()
                        child.depth = node.depth + 1
                        child.data = rot
                        child.move = "{0}/{1} {2}r".format(i + 1, j + 1, k + 1)
                        node.children.append(child)
                        fringe.append(child)
                
        if (len(fringe) > 0) :
            node = fringe.popleft()

    return root

def minMax(node, maxOrMin, maxDepth) :

    if (node.depth == maxDepth) :
        return node.data.heuristicValue()
    

    if (maxOrMin) :
        bestH = -sys.maxsize
        for child in node.children :
            value = minMax(child, False, maxDepth)
            bestH = max(bestH, value)
        return bestH
    else :
        bestH = sys.maxsize
        for child in node.children :
            value = minMax(child, True, maxDepth)
            bestH = min(bestH, value)
        return bestH



    



# inner class used to represent nodes on tree
class Node(object):
    def __init__(node):
        node.data = None
        node.depth = None
        node.parent = None
        node.children = []
        node.move = ""

    def __repr__(self) :
        result = ""


        return result
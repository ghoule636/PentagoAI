"""
# Gabriel Houle
# Programming Assignment 2
# TCSS 435 AI Spring 2016
"""
from collections import deque
import sys

global created

def decideMoveMinMax(state, maxDepth, type) :
    global created
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
    #print("Nodes created: {0}".format(created))
    return moveTree.children[bestIndex].move

def decideMoveAlphaBeta(state, maxDepth, type) :
    global created
    created = 0
    root = Node()
    root.depth = 0
    root.data = state
    if (type == 'w') :
        alphaBeta(root, type, maxDepth, True, -sys.maxsize, sys.maxsize)
        bestMove = -sys.maxsize
        for i in range(len(root.children)) :
            if (root.children[i].alphaBetaValue > bestMove) :
                bestMove = root.children[i].alphaBetaValue
                bestIndex = i

    else :
        alphaBeta(root, type, maxDepth, False, -sys.maxsize, sys.maxsize)
        bestMove = sys.maxsize
        for i in range(len(root.children)) :
            if (root.children[i].alphaBetaValue < bestMove) :
                bestMove = root.children[i].alphaBetaValue
                bestIndex = i

    #print("root a/b value: ", root.alphaBetaValue)
    #print("best child value: ", bestMove)
    #print("Nodes created: {0}".format(created))

    return root.children[bestIndex].move
    

# creates tree of moves up to maximum depth for minmax
def createTree(state, maxDepth, type) :
    global created
    root = Node()

    root.depth = 0
    root.data = state
    fringe = deque()

    node = root
    created = 0
    while (node.depth < maxDepth) :
        #print(created)
        if (node.depth % 2 != 0) :
            if (type == 'b') :
                addPiece == 'w'
            else :
                addPiece == 'b'
        else :
            addPiece = type
        for i in range(4) :
            for j in range(9) :
                pos = node.data.copyBoard()
                canMove = pos.addPiece(i + 1, j + 1, addPiece)

                if (canMove) :
                    for k in range(1, 5) :
                        created += 2
                        rot = pos.copyBoard()
                        rot.shiftLeft(k)

                        child = Node()
                        child.depth = node.depth + 1
                        child.data = rot
                        child.move = "{0}/{1} {2}l".format(i + 1, j + 1, k)
                        node.children.append(child)
                        fringe.append(child)
                            
                        rot = pos.copyBoard()
                        rot.shiftRight(k)
                        child = Node()
                        child.depth = node.depth + 1
                        child.data = rot
                        child.move = "{0}/{1} {2}r".format(i + 1, j + 1, k)
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

def alphaBeta(node, type, maxDepth, maxOrMin, alpha, beta) :
    global created
    if (node.depth >= maxDepth) :
        node.alphaBetaValue = node.data.heuristicValue()
        return
    if (type == 'b') :
        nextPiece = 'w'
    else :
        nextPiece = 'b'
    for i in range(4) :
        for j in range(9) :
            pos = node.data.copyBoard()
            canMove = pos.addPiece(i + 1, j + 1, type)

            if (canMove) :
                for k in range(1, 5) :
                    created += 1
                    rot = pos.copyBoard()
                    rot.shiftLeft(k)

                    child = Node()
                    child.depth = node.depth + 1
                    child.data = rot
                    child.move = "{0}/{1} {2}l".format(i + 1, j + 1, k)
                    node.children.append(child)
                    
                    alphaBeta(child, nextPiece, maxDepth, not maxOrMin, alpha, beta)
                    if (maxOrMin) :
                        if (child.alphaBetaValue > alpha) :
                            alpha = child.alphaBetaValue
                            node.alphaBetaValue = alpha
                    else :
                        if (child.alphaBetaValue < beta) :
                            beta = child.alphaBetaValue
                            node.alphaBetaValue = beta
                    if (alpha >= beta) :

                        return

                    created += 1
                    rot = pos.copyBoard()
                    rot.shiftRight(k) 

                    child = Node()
                    child.depth = node.depth + 1
                    child.data = rot
                    child.move = "{0}/{1} {2}r".format(i + 1, j + 1, k)
                    node.children.append(child)
                    alphaBeta(child, nextPiece, maxDepth, not maxOrMin, alpha, beta)
                    if (maxOrMin) :
                        if (child.alphaBetaValue > alpha) :
                            alpha = child.alphaBetaValue
                            node.alphaBetaValue = alpha
                    else :
                        if (child.alphaBetaValue < beta) :
                            beta = child.alphaBetaValue
                            node.alphaBetaValue = beta
                    if (alpha >= beta) :
                        return
    if (node.alphaBetaValue == None) :
        if (maxOrMin) :
            bestValue = -sys.maxsize
            bestIndex = 0
            for j in range(len(node.children)) :
                if (node.children[j].alphaBetaValue > bestValue) :
                    bestValue = node.children[j].alphaBetaValue
        else :
            bestValue = sys.maxsize
            bestIndex = 0
            for j in range(len(node.children)) :
                if (node.children[j].alphaBetaValue < bestValue) :
                    bestValue = node.children[j].alphaBetaValue
        node.alphaBetaValue = bestValue

    return

# inner class used to represent nodes on tree
class Node(object):
    def __init__(node):
        node.data = None
        node.depth = None
        node.parent = None
        node.alphaBetaValue = None
        #node.alpha = -sys.maxsize
        #node.beta = sys.maxsize
        node.children = []
        node.move = ""

    def __repr__(self) :
        return str(self.data)
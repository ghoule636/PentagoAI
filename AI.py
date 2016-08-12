"""
# Gabriel Houle
# Programming Assignment 2
# TCSS 435 AI Spring 2016
"""

def decideMove(state, maxDepth) :
    result = ""
    moveTree = createTree(state, maxDepth)

    return result



def createTree(state, maxDepth) :
    result = Node()

    print(state.heuristicValue())

    return result


# inner class used to represent nodes on tree
class Node(object):
    def __init__(node):
        node.children = None
        node.data = None
        node.depth = None
        node.parent = None

    def __repr__(self) :
        result = ""


        return result
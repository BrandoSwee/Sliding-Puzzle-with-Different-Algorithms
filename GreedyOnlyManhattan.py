# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 16:36:40 2021

@author: Brandon
"""
import copy
from board import Board
from Node import Node
#import numpy as np

#GOAL = Board(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]))
#extra = Board(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]))
#start = Board(np.array([[1,3,7,4], [6,2,0,8], [5,9,11,12], [13,10,14,15]]))
# Performs Greedy Best-First Search using the Manhattan Distance heuristic.
def Greedy(s, G):
    GOAL = Board(G)
    start = Board(s)
    hv = start.Hv(GOAL)
    visitedStates = [Node(start,None,hv,0)]
    pq = []
    pq.append([hv, Node(start,None,hv,0)])
    nodesExpanded = 0

    while len(pq) > 0:
        # https://stackoverflow.com/questions/36955553/sorting-list-of-lists-by-the-first-element-of-each-sub-list
        # Used for sorting the list of Nodes.
        pq = sorted(pq, key=lambda x: x[0])
        state = pq.pop(0)
        boardState = state[1].state
        if(state[1].hv == 0):
            d = state[1].cost
            path = []
            state = state[1]
            path.append(state)
            while(state.parent != None):
                state = state.parent
                path.append(state)
            while(len(path) > 0):
                state = path.pop() # equivalent to -1
                print("Depth", state.cost)
                print(state.state)
            print("Found a solution at depth" , d)
            print(nodesExpanded , "Nodes expanded.")
#           print(len(visitedStates) - nodesExpanded , "Nodes not expanded.")
            print(len(visitedStates), "Nodes in total.")
            n = len(visitedStates)
            return d,nodesExpanded,n

        boardState.up(state[1],copy.deepcopy(boardState), pq, visitedStates, GOAL, "G")
        boardState.right(state[1],copy.deepcopy(boardState), pq, visitedStates, GOAL, "G")
        boardState.down(state[1],copy.deepcopy(boardState), pq, visitedStates, GOAL, "G")
        boardState.left(state[1],copy.deepcopy(boardState), pq, visitedStates, GOAL, "G")
        nodesExpanded += 1
    return 0,0,0
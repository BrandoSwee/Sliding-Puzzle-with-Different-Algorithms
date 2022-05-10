# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 12:19:18 2021

@author: Brandon
"""
import copy
from board import Board
from Node import Node
#import numpy as np
#GOAL = Board(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]))
#extra = Board(np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]))
#start = Board(np.array([[1,3,7,4], [6,2,0,8], [5,9,11,12], [13,10,14,15]]))
# Preforms Breadth-First Search on a start and goal.
def BFS(s, G):
    GOAL = Board(G)
    start = Board(s)
    visitedStates = [Node(start,None,0,0)]
    q = []
    q.append(Node(start,None,0,0))
    nodesExpanded = 0
    m = 0
    while len(q) > 0:
        state = q.pop(0)
        boardState = state.state
        if(state.cost < m):
            print("ERROR occured")
            return 0,0,0
        if(state.cost > m):
            m = state.cost
            print("Hit depth ", m)
        if((boardState.Compare(GOAL) == True)):
            d = state.cost
            path = []
            path.append(state)
            while(state.parent != None):
                state = state.parent
                path.append(state)
            while(len(path) > 0):
                state = path.pop() # equivalent to -1
                print("Depth", state.cost)
                print(state.state)
            print("Found a solution at depth" , d)
            print(nodesExpanded , "Nodes expanded")
            #Not needed
#           print(len(visitedStates) - nodesExpanded , "Nodes not expanded")
            print(len(visitedStates), "Nodes in total.")
            n = len(visitedStates)
            return d,nodesExpanded,n
    
        boardState.up(state,copy.deepcopy(boardState), q, visitedStates, GOAL, "B")
        boardState.right(state,copy.deepcopy(boardState), q, visitedStates, GOAL, "B")
        boardState.down(state,copy.deepcopy(boardState), q, visitedStates, GOAL, "B")
        boardState.left(state,copy.deepcopy(boardState), q, visitedStates, GOAL, "B")
        nodesExpanded += 1
    return 0,0,0
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 12:19:18 2021

@author: Brandon
"""
#################################
#   Brandon Sweeney
#   Assignment 1
#   9 - 9 - 2021
#   15 - Puzzle
#################################
# My python I/O might have issues.
# Main is the last thing I made.
import numpy as np
from Astar import Astar
from GreedyOnlyManhattan import Greedy
from bfs import BFS
print("Welcome to the 15-Puzzle search technique comparison program.")
print("Warning: There is no parity checking so it's recommended that you input values")
print("or use the example. You can also change the example for your own input as it may be easier.")
print("Do you want to input values, randomize them, or use the example?")
print("~ is anything other than i or r.")
userChoice = input("i / r / ~: ")
Good = True
start = []
goal = []
#extra = np.array([[1,3,7,4], [6,2,0,8], [5,9,11,12], [13,10,14,15]])
if(userChoice == "i" or userChoice == "I"):
    print("Please enter your start board one number at a time starting from the top left.")
    print("Order Example:\n 1 2 3 4\n 5 6 7 8\n 9 10 11 12\n 13 14 15 16")
    for i in range(1, 17):
        userNum = input("Number:")
        userNum = int(userNum)
        if(userNum >= 0 and userNum < 16 and userNum not in start):
            start.append(userNum)
        else:
            print("Number is not in range (0,15) or already in start.")
            Good = False
            break
    if(Good):
        print("Now enter you goal board one number at a time in the same fashion as the start board.")
        for i in range(1, 17):
            userNum = input("Number:")
            userNum = int(userNum)
            if(userNum >= 0 and userNum < 16 and userNum not in goal):
                goal.append(userNum)
            else:
                print("Number is not in range (0,15) or already in goal.")
                Good = False
                break
    if(Good):
        e = np.array(start)
        e = np.array_split(e, 4)
        start = np.array([e[0],e[1],e[2],e[3]])
        e = np.array(goal)
        e = np.array_split(e, 4)
        goal = np.array([e[0],e[1],e[2],e[3]])
elif(userChoice == "r" or userChoice == "R"):
    start = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    goal = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
    start = np.array(start)
    np.random.shuffle(start)
    start = np.array_split(start, 4)
    start = np.array([start[0],start[1],start[2],start[3]])
    goal = np.array(goal)
    np.random.shuffle(goal)
    goal = np.array_split(goal, 4)
    goal = np.array([goal[0],goal[1],goal[2],goal[3]])
else:    
    goal = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]])
    start = np.array([[1,3,7,4], [6,2,0,8], [5,9,11,12], [13,10,14,15]])
if(Good):
    print("Your Boards are:")
    print("Start")
    print(start)
    print("Goal")
    print(goal)
    print("We will start with A*.")
    ### I will use these for a final comparison.
    Astard = 0 #Depth
    Astare = 0 #expanded
    Astarn = 0 #nodes
    Gd = 0
    Ge = 0
    Gn = 0
    BFSd = 0
    BFSe = 0
    BFSn = 0
    ## I figure starting with Astar will help me stop the program early if
    ## the board is unsolvable.
    Astard, Astare, Astarn = Astar(start, goal)
    print("Greedy next")
    Gd, Ge, Gn = Greedy(start, goal)
    print("BFS last")
    BFSd, BFSe, BFSn = BFS(start, goal)
    print("Your boards were")
    print("Start")
    print(start)
    print("Goal")
    print(goal)
    print("Table of results:")
    a = ["Astar",Astard,Astare,Astarn]
    g = ["Greedy",Gd,Ge,Gn]
    b = ["BFS",BFSd,BFSe,BFSn]
    top = ["SearchTech","DepthOfSolution","NodesExpanded", "NodesInTotal"]
    results = np.array([top,a,g,b])
    print(results)
    
    
else:
    print("Please try again.")

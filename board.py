# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:34:28 2021

@author: Brandon
"""
from Node import Node
import numpy as np

# Board holds a numpy array
class Board(object):
    def __init__(self,b):
        self.b = b
    # numpy arrays print like this:
    # [[ 1  2  3  4]
    #  [ 5  6  7  8]
    #  [ 9 10 11 12]
    #  [13 14 15  0]]
    # Note: I didn't know numpy had a repr.
    # This replaces board's print.
    # So calling prints gives this board's repr. Calling print on board.b
    # will give the numpy repr.     
    def __repr__(self):
        s = ''
        for x in self.b:
            for num in x:
                if(len(str(num)) == 1):
                    s += ' ' + str(num)
                elif(len(str(num)) > 1):
                    s += ' ' + str(num)
            s += '\n'
        return s
    # Made for BFS to see if I had made it to goal.
    # Still used in movement methods to see if the board is in the visitedList.
    def Compare(self, other):
        if(np.array_equal(self.b,other.b)):
            return True
        else:
            return False
    # Used for calculating Manhattan Distance heuristic value.
    def Hv(self, goal):
        hv = 0
        for i in range(1, 16):
            numS = np.where(self.b == i)
            xS = numS[0][0]
            yS = numS[1][0]
            numG = np.where(goal.b == i)
            xG = numG[0][0]
            yG = numG[1][0]
            if(xS == xG):
                hv += 0
            else:
                diff = abs(xG - xS)
                hv += diff
            if(yS == yG):
                hv += 0
            else:
                diff = abs(yG - yS)
                hv += diff
        return hv
############################################################################
### These are for BFS only.
### Most of this is very similar to the other.
### So I just adjusted the other one.        
#    def up(self, pN, other, q, v):
#        blank = np.where(self.b == 0)
#        x = blank[0][0]
#        y = blank[1][0]
#        if (x != 0):
#            temp = other.b[x - 1][y]
#            other.b[x][y] = temp
#            other.b[x - 1][y] = 0
#            for i in range(len(v)):
#                if((other.Compare(v[i].state) == True)):
#                    return False
#            newNode = Node(other,pN,0,pN.cost + 1)
#            v.append(newNode)
#            q.append(newNode)
#
#    def right(self, pN, other, q, v):
#        blank = np.where(self.b == 0) 
#        x = blank[0][0]
#        y = blank[1][0]    
#        if (y != 3):        
#            temp = other.b[x][y + 1]
#            other.b[x][y] = temp
#            other.b[x][y + 1] = 0
#            for i in range(len(v)):
#                if((other.Compare(v[i].state) == True)):
#                    return False
#            newNode = Node(other,pN,0,pN.cost + 1)
#            v.append(newNode)
#            q.append(newNode)
#                    
#    def down(self, pN, other, q, v):
#        blank = np.where(self.b == 0)
#        x = blank[0][0]
#        y = blank[1][0]    
#        if (x != 3):
#            temp = other.b[x + 1][y] 
#            other.b[x][y] = temp
#            other.b[x + 1][y] = 0
#            for i in range(len(v)):
#                if((other.Compare(v[i].state) == True)):
#                    return False
#            newNode = Node(other,pN,0,pN.cost + 1)
#            v.append(newNode)
#            q.append(newNode)
#
#    def left(self, pN, other, q, v):
#        blank = np.where(self.b == 0) 
#        x = blank[0][0]
#        y = blank[1][0]    
#        if (y != 0):        
#            temp = other.b[x][y - 1]
#            other.b[x][y] = temp
#            other.b[x][y - 1] = 0
#            for i in range(len(v)):
#                if((other.Compare(v[i].state) == True)):
#                    return False
#            newNode = Node(other,pN,0,pN.cost + 1)
#            v.append(newNode)
#            q.append(newNode)
##############################################################
### These were named MDup, MDright, MDdown, and MDleft
### But now all methods call these.
    def up(self, pN, other, pq, v, goal, Type):
        blank = np.where(self.b == 0)
        x = blank[0][0]
        y = blank[1][0]
        if (x != 0):
            temp = other.b[x - 1][y]
            other.b[x][y] = temp
            other.b[x - 1][y] = 0
            for i in range(len(v)):
                if((other.Compare(v[i].state) == True)):
                    return False
            if(Type == "B"):
                ### I keep Hv 0 throughout BFS
                newNode = Node(other,pN,0,pN.cost + 1)
                v.append(newNode)
                pq.append(newNode)
            else:
                HV = other.Hv(goal)
                newNode = Node(other,pN,HV,pN.cost + 1)
                v.append(newNode)
                if(Type == "A"):
                    pq.append([(HV + (pN.cost + 1)), newNode])
                else:
                    pq.append([HV, newNode])
                    
    def right(self, pN, other, pq, v, goal, Type):
        blank = np.where(self.b == 0) 
        x = blank[0][0]
        y = blank[1][0]    
        if (y != 3):        
            temp = other.b[x][y + 1]
            other.b[x][y] = temp
            other.b[x][y + 1] = 0
            for i in range(len(v)):
                if((other.Compare(v[i].state) == True)):
                    return False
            if(Type == "B"):
                newNode = Node(other,pN,0,pN.cost + 1)
                v.append(newNode)
                pq.append(newNode)
            else:
                HV = other.Hv(goal)
                newNode = Node(other,pN,HV,pN.cost + 1)
                v.append(newNode)
                if(Type == "A"):
                    pq.append([(HV + (pN.cost + 1)), newNode])
                else:
                    pq.append([HV, newNode])
                
    def down(self, pN, other, pq, v, goal, Type):
        blank = np.where(self.b == 0) 
        x = blank[0][0]
        y = blank[1][0]    
        if (x != 3):        
            temp = other.b[x + 1][y]
            other.b[x][y] = temp
            other.b[x + 1][y] = 0
            for i in range(len(v)):
                if((other.Compare(v[i].state) == True)):
                    return False
            if(Type == "B"):
                newNode = Node(other,pN,0,pN.cost + 1)
                v.append(newNode)
                pq.append(newNode)
            else:
                HV = other.Hv(goal)
                newNode = Node(other,pN,HV,pN.cost + 1)
                v.append(newNode)
                if(Type == "A"):
                    pq.append([(HV + (pN.cost + 1)), newNode])
                else:
                    pq.append([HV, newNode])
                
    def left(self, pN, other, pq, v, goal, Type):
        blank = np.where(self.b == 0) 
        x = blank[0][0]
        y = blank[1][0]    
        if (y != 0):        
            temp = other.b[x][y - 1]
            other.b[x][y] = temp
            other.b[x][y - 1] = 0
            for i in range(len(v)):
                if((other.Compare(v[i].state) == True)):
                    return False
            if(Type == "B"):
                newNode = Node(other,pN,0,pN.cost + 1)
                v.append(newNode)
                pq.append(newNode)
            else:
                HV = other.Hv(goal)
                newNode = Node(other,pN,HV,pN.cost + 1)
                v.append(newNode)
                if(Type == "A"):
                    pq.append([(HV + (pN.cost + 1)), newNode])
                else:
                    pq.append([HV, newNode])
#####################################################################
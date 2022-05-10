# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:55:36 2021

@author: Brandon
"""
## The node is used to hold all important values.
# state is a board object.
# parent is a Node object.
# hv is the heuristic value.
# cost is the depth in the tree.
class Node(object):
    def __init__(self, x, parNode, hv, cost):
        self.state = x
        self.parent = parNode
        self.hv = hv
        self.cost = cost
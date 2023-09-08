#!/bin/python3

import math
import os
import random
import re
import sys

# Node class for a binary tree node
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
#
#   -Breadth first search (BFS)
#		-Explore each level before moving to the next level
#		-Explore all nodes on the current level
#		-Move on to the next level
#
#
# Complete the 'treeBFS' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts TreeNode root as parameter.
#
# Pseudocode:
# create result [];
# if root is null:
#        return result
#
# create queue 
# enqueue root 
#
# while queue is not empty
#   curr = dequeue
#   enqueue non null children of curr
#   add curr.value to result array
#
import threading, queue
def treeBFS(root):
    # Write your code here
    result = []
    if root == None:
        return result
    q = queue.Queue()
    q.put(root)
    while q.qsize() > 0:
        curr = q.get()
        if curr.left : q.put(curr.left)
        if curr.right : q.put(curr.right)
        result.append(curr.value)
    return result

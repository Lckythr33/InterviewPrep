class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
#
#   -Depth first search (DFS)  //use recursion for DFS
#       -Traverse as far as you can along each branch
#		-Back out of that branch
#		-Pick other branches to explore, start at step 1 again
#

#DFS Order Traversals

# Operations:
# left traversal
# right traversal
# *action

#Pre-Order   //the action before PRE
#   *action   // process parents before children
#   left traversal
#   right traversal

#Post-Order  // the action after POST
#   left traversal  //process children before parents
#   right traversal
#   *action

#In-Order // the action in the middle IN
#   left traversal // Incrementing order if binary search tree
#   *action
#   right traversal

#In-Reverse-Order // Decrementing order if binary search tree
#   right traversal
#   *action
#   left traversal

def preDFS(root):
    result = []
    # Write your code here
    def traverse(curr):
        if curr == None:
            return 
        result.append(curr.value)
        traverse(curr.left)
        traverse(curr.right)
        
    traverse(root)
    return result

def inDFS(root):
    # Write your code here
    result = []
    # Write your code here
    def traverse(curr):
        if curr == None:
            return 
   
        traverse(curr.left)
        result.append(curr.value)
        traverse(curr.right)
        
    traverse(root)
    return result

def postDFS(root):
    # Write your code here
    result = []
    # Write your code here
    def traverse(curr):
        if curr == None:
            return 
    
        traverse(curr.left)
        traverse(curr.right)
        result.append(curr.value)
        
    traverse(root)
    return result



#Prevent Cycles

# create a set DS
# Add curr to visited
# Only traverse to visited edges

import queue
def treeBFS(root):
    # Write your code here
    result = []
    if root == None:
        return result
    q = queue.Queue()
    q.put(root)
    visited = {}
    visited.append(root)

    while q.qsize() > 0:
        curr = q.get()

#iterate thorugh edges
    for edge in curr.edges:
        if(not visited.has(edge)):
            q.put(root)
            visited.append(edge)

    return result


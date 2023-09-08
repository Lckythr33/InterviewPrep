# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
#Input:
#              4
#       /              \
#       2                7
#   /       \          /    \
#   1        3         6    9
#
#
#
#Output:
#              4
#       /              \
#       7               2
#   /       \          /    \
#   9       6        3      1
#
#
#
# Tree Traversals: (tree is a type of graph)
#   -Depth first search (DFS)  //use recursion for DFS
#       -Traverse as far as you can along each branch
#		-Back out of that branch
#		-Pick other branches to explore, start at step 1 again
#
#   -Breadth first search (BFS)
#		-Explore each level before moving to the next level
#		-Explore all nodes on the current level
#		-Move on to the next level
#



class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(curr):
            if curr == None: 
                return
            
            #swap
            swap = curr.left
            curr.left = curr.right
            curr.right = swap  
            
            #traverse
            dfs(curr.left)
            dfs(curr.right)
            
        dfs(root)
        return root

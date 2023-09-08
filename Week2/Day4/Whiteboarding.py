# Longest Path of a Binary Tree
# Given a binary tree node, return the number of nodes in the longest path between the root and a leaf node

# Input: Node in a Binary Tree
# Output: Integer

# Time Complexity: O(N)
# Auxiliary Space Complexity: O(N)

DFS
-how tall is the tree
return height of tree

Post order traversal

return 1 

height of a tree given by returning 1 for each level

#PSEUDO
def postDFS(root):
    def traverse(curr):
        if curr == None:
            return 
        traverse(curr.left)
        #find total of left branch
        lcount += 1
        traverse(curr.right)
        #find total of right branch
        rcount += 1
      #compare which branch is taller
    if lcount < rcount
      return rcount
    
    return lcount
    
    traverse(root)


      3                          4
     1               5            1
              /           \ 
     1       1              6      1
          / \              / \
     1   2 3              7  8      1
                               \
                                9    1

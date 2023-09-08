
# Complete the 'powerset' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING word as parameter.
#
#Helper Method Recursion
#Create State Variables
#Return State Variables
#Instantiate and invoke helper method
#Base case 
#Recursive case 

def powerset(word):
    # Write your code here
    result = []
    
    def findCombos(build,depth):
        if depth == len(word):
            result.append(build)
            return
        #left    
        findCombos(build,depth+1) #how does the left of the tree change
        #right
        findCombos(build + word[depth],depth+1) # how does the right of the tree change
        
    findCombos("",0)  

    return result
    
print(powerset("abc"))

def latticePaths(m, n):
    # Write your code here
    #base cases
    if m <  0 or n < 0: 
        return 0
    if m == 0 and n == 0:
        return 1
    
    #return with motion on tree , (make tree move)
    up = latticePaths(m-1,n)
    left = latticePaths(m,n-1)
    
    return up+left

    
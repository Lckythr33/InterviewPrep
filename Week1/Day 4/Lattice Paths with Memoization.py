from functools import cache

#Change from Lattice Paths without Cache to Cached answer

#memoization
#1)Create a cache
#2)Check the cache
#3)Populate the cache


def lattice_paths(m, n):

    cache={} #create a cache

    def find_paths(m,n):

        if (m,n) in cache:   # Check the cache
            return cache[(m,n)] #return findings

        # if (n,m) in cache:            optimization to cut off half the tree, 
        #     return cache[(n,m)]       because we notice this tree is mirror on both sides

        #base cases
        if m <  0 or n < 0: 
            return 0
        if m == 0 and n == 0:
            return 1
        
        #return with motion on tree , (make tree move)
        up = find_paths(m-1,n)
        left = find_paths(m,n-1)
        
        cache[(m,n)] = up + left #populate the cache
        return cache[(m,n)] # return the cache findings

    return find_paths(m,n)

print(lattice_paths(100,100))



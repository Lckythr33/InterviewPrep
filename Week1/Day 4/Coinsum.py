# Recognizing Recursion:
# 1)is there a smallest case?
# 2)can this smallest case be used to solve incrementally larger verisons of the same problem
# 3)permutations/combinations

# Basically putting the cache in a 2D matrix

# Tabulation: (IS AN ITERATIVE SOLUTON THAT IS INSPIRED BY RECURSION)
# 1)Identify parameters (m,n)
# 2)Create a table with incrementally increasing factors
# 3)Determine a formula (recursive relationship)
# 4)Build foundation - first row / "base cases"
# 5)Fill out the table

# Coin sum

# [1,2,4] , 5
# coins     total

# Want to know how many ways we can make change with those coins

# Recursive Tree
#
#        Always consider the last coin so we dont have to shift the array
#     
#                                                        5 , [1,2,4]
#                          /                                                                 \
#                       1 , [1,2,4]                                                          5,[1,2]
#                    /          \
#               -3, [1,2,4]     1,[1,2]
#                               /        \ 
#                            0,[1,2]        1,[1]
#                           / \         /           \
#                          -2,[1,2]    0,[1]        0,[] #base case
#                                       /               
#                                   -1,[1]
#
#       Base Cases: 
#          if total == 0 && [] no coins remain 
#           return 1
#
#       Failure case:
#          if total < 0 
#           return 0
#          if total > 0 && [] no coins remain
#           return 0
#       
#      Recursive Cases:
#           either we use the last coin
#           or we dont and never use it again

#memoization
#1)Create a cache
#2)Check the cache
#3)Populate the cache

def coin_sum(coins,total):

    cache = {}
    
    def traverse(i,total):
        if(i,total) in cache:
            return cache[(i,total)]

        if total == 0:
            return 1
        if total < 0 or (total > 0 and  i < 0):
            return 0
        
        #use coin at i
        left = traverse(i,total-coins[i])
        # dont use coin at i
        right = traverse(i-1,total)

        cache[(i,total)] = left+right
        return cache[(i,total)]

    return traverse(len(coins)-1,total)

print(coin_sum([1,2,4],8))


# Tabulation: (IS AN ITERATIVE SOLUTON THAT IS INSPIRED BY RECURSION)
# 1)Identify parameters (m,n)
# 2)Create a table with incrementally increasing factors
# 3)Determine a formula (recursive relationship)
# 4)Build foundation - first row / "base cases"
# 5)Fill out the table


#                   0   1   2   3   4   5
#          index    ---------------------
#   []      -1    | 1   0   0   0   0   0     
#   [1]      0    | 1   1   1   1   1   1 
#   [1,2]    1    | 1   1   2   2   3   3           look above and to the left, we are reducing a coin and subtracting from the total
#   [1,2,4]  2    | 1   1   2   2   4   4           the amount we go left is related to the coin we are considering subtracting

#Time complexity  : o(m*n)
#Space complexity : o(m*n)

# index = 2 | coin value = 4  #walk through make sure it works
#   0 1 2 3 4 5
# [ 1 1 2 2 4 4 ]  #UPDATE ARRAY NO MATRIX NEEDED AS WE ONLY LOOK 1 ROW UP

def tab_coin_sum(coins,total):
    arr = [0] * (total+1)
    arr[0] = 1

    for coin in coins:
        for j in range(coin,total+1):
            arr[j] += arr[j-coin]

    return arr[total]

print(tab_coin_sum([1,2,4],5))

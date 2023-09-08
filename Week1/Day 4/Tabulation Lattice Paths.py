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

# table diagram:

#         0 1 2
#         -----
#     0 | 1 1 1   look up and to the left to determine the next answer
#     1 | 1 2 3
#     2 | 1 3 6

# you can use a single array in place instead of a matrix for this one
# as you are summing the one above which would be itself with the one on the left
# so you only have to sum the one on the left and return
# keep updating until you reach [1,3,6]

def tab_paths(m,n):
    table = [1] * (n+1) #list of ones and how many you want of them

    for _ in range (m):
        for i in range(1,n+1):  #+1 to include final element
            table[i] += table[i-1]

    return table[n]

print(tab_paths(100,100))


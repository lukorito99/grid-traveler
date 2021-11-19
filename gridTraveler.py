''' A traveler on a 2D grid,begin in the topleft corner and goal is to travel
to the bottom right corner.Restricted to moving only down or right.

How many ways can you travel to the goal on a grid with dimensions m * n?'''

#Correctness
def travel(i, j): #time complexity = O(2**(i+j))
    # base case
    if i == 1 and j == 1:
        return 1

    # invalid
    if i == 0 or j == 0:
        return 0

    return travel(i - 1, j) + travel(i, j - 1)


# travel(i,j) == travel(j,i)
# dynamic_travel(i,j) == dynamic_travel(j,i)


# employs memoization-efficiency
def dynamic_travel(i, j, memo=dict()): # time complexity = O(i*j)
    k = str(i) + ',' + str(j)

    if k in memo:
        return memo[k]

    # base case
    if i == 1 and j == 1:
        return 1

    # invalid
    if i == 0 or j == 0:
        return 0

    memo[k] = dynamic_travel(i - 1, j, memo) + dynamic_travel(i, j - 1, memo)
    return memo[k]

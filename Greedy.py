print """  
Milad Pejmanrad (mp0406)

I have shown two different trials with different starting points. 
You can easily try different trials by moving the 0 value in the grid, except the cells that has a value of -1 which are the walls.

This is the logic behind choosing the values of each cell:

Start = 0
White blocks = 1
Black blocks = -1
Yellow blocks = 2
Goal(s) = 9

"""
print "---------------------------------------------------------------------------------\n   \t\t\t\t -----The first trial-----"

print "---------------------------------------------------------------------------------"
import numpy
from numpy import linalg as LA
import copy

# The grid for the first trial
grid = [
    [ 0,  1,  1, -1,  1,  2,  2,  2,  2,  2,  2,  2],
    [ 1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2],
    [ 1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1],
    [ 1, -1,  1,  1,  1, -1, -1,  1,  1,  9,  1,  1],
    [ 1, -1,  1,  1,  1,  1,  1, -1,  1,  1,  1,  1],
    [ 1, -1,  2,  2,  1,  1,  1,  1, -1, -1,  1,  1],
    [ 1,  1,  2,  2,  2,  1,  1,  1,  9, -1,  1,  1],
    [ 2,  2,  2,  2,  2,  1,  1,  1,  1,  1,  1,  1],
    [ 2,  2,  2,  2,  2,  1,  1,  1,  1,  1,  1,  1],
    [ 1,  1,  2,  2,  2,  1,  1,  1,  1,  1,  1,  1]]

# The grid for the second trial
grid_B = [
    [ 1,  1,  1, -1,  1,  2,  2,  2,  2,  2,  2,  2],
    [ 1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2],
    [ 1, -1,  1,  1, -1, -1,  1, -1, -1,  1,  1,  1],
    [ 1, -1,  1,  1,  1, -1, -1,  1,  1,  9,  1,  1],
    [ 1, -1,  1,  1,  1,  1,  1, -1,  1,  1,  1,  1],
    [ 1, -1,  2,  2,  1,  1,  1,  1, -1, -1,  1,  1],
    [ 1,  1,  2,  2,  2,  1,  1,  1,  9, -1,  1,  1],
    [ 2,  2,  2,  2,  2,  1,  1,  1,  1,  1,  1,  1],
    [ 2,  2,  2,  2,  2,  1,  1,  1,  1,  1,  1,  1],
    [ 0,  1,  2,  2,  2,  1,  1,  1,  1,  1,  1,  1]]

# Storing the dimensions of the grid
x = len(grid) - 1
y = len(grid[0]) - 1

# Finding the location of the Starting point
for i in range(x+1):
    for j in range(y+1):
        if grid[i][j] == 0:
            s = [[i, j]]
            break
goals = []
# Finding the location of the goal(s)
for i in range(x+1):
    for j in range(y+1):
        if grid[i][j] == 9:
            goals.append([i, j])


#building heuristics based on Euclidean distance 
heuristics = copy.deepcopy(grid)
for i in range(x+1):
    for j in range(y+1):
        if grid[i][j] != 9:
            if grid[i][j] == -1:
                heuristics[i][j] = -1
            else:
                numbers = []
                for goal in goals:
                    a = numpy.array([i,j])
                    b = numpy.array([goal[0],goal[1]])
                    numbers.append(numpy.linalg.norm(a-b))
                heuristics[i][j] = min(numbers)
        else:
            heuristics[i][j] = 0


def check(i, j, traversed): # To check if a certain pair of indices exists in the traversed list
    for node in traversed:
        if node[0] == i and node[1] == j:
            return True
    return False



# Building a tree-like array to keep track of all the paths explored
def add_to_path(i, j, ip, jp, paths):
    for path in paths:
        if path[-1][0] == ip and path[-1][1] == jp:
            break
    path1 = copy.deepcopy(path)
    path1.append([i,j])
    paths.append(path1)
    return paths
    
    
# Given a cell, this function returns all possible neighbours and their cost
def neighbours(i,j):
    n = []
    
    # Checking for the right neighbour
    if j < y:
        if grid[i][j+1] != -1:
            n.append([i,j+1])

    # Checking for the left neighbour
    if j > 0:
        if grid[i][j-1] != -1:
            n.append([i, j-1])
    
    # Checking for the upper neighbour
    if i > 0:
        if grid[i-1][j] != -1:
            n.append([i-1, j])
    
    # Checking for the lower neighbour
    if i < x:
        if grid[i+1][j] != -1:
            n.append([i+1, j])
    return n
            


def Greedy(traversed, solution_length, grid, paths):
    numbers = []
    for node in neighbours(traversed[-1][0], traversed[-1][1]):
        if node not in traversed:
            if grid[node[0]][node[1]] == 9:
                add_to_path(node[0], node[1], traversed[-1][0], traversed[-1][1], paths)
                for path in paths:
                    if path[-1][0] == node[0] and path[-1][1] == node[1]:
                        break
                traversed.append(node)
                # Printing the original board
                print "The original board:\n"
                for row in grid:
                    for val in row:
                        print '{:4}'.format(val),

                    print 
                print
                print "The algorithm used here is Greedy.\n"
                print "The heuristics used is Euclidean distance.\n"
                print "The heuristics board:(I put -1 for the heuristic of the walls)\n"
                for row in heuristics:
                    for val in row:
                        print '{:4}'.format(int(val)),

                    print 
                print
                grid_changed = copy.deepcopy(grid)
                for i in range(x+1):
                    for j in range(y+1):
                        if [i, j] not in path:
                            grid_changed[i][j] = -1
                number = 0
                for node in path:
                    grid_changed[node[0]][node[1]] = number
                    number += 1

                print "Number of nodes explored:", len(path)
                print
                print "Solution length:", solution_length
                print 
                print "The solution path which starts from 0 and ends in {} which is the goal location:\n".format(len(traversed)-1)
                for row in grid_changed:
                    for val in row:
                        if val != -1:
                            print '{:4}'.format(val),
                        else:
                            print '{:4}'.format(""),
                    print
                return
            
            else:
                add_to_path(node[0], node[1], traversed[-1][0], traversed[-1][1], paths)
                numbers.append([grid[node[0]][node[1]] + int(heuristics[node[0]][node[1]]), node[0], node[1]]) 

    
    minimum = 99999
    for number in numbers:
        if number[0] < minimum:
            minimum = number[0]
            node = [number[1], number[2]]
    solution_length = solution_length + grid[node[0]][node[1]]
    traversed.append(node)
    Greedy(traversed, solution_length, grid, paths)

Greedy(s, 0, grid, [[[s[0][0], s[0][1]]]])   
print 
print "---------------------------------------------------------------------------------\n   \t\t\t\t -----The second trial-----"

print "---------------------------------------------------------------------------------"

# Finding the location of the Starting point
for i in range(x+1):
    for j in range(y+1):
        if grid_B[i][j] == 0:
            s = [[i, j]]
            break
            
Greedy(s, 0, grid_B, [[[s[0][0], s[0][1]]]])  
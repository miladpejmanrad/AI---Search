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
import copy

print "---------------------------------------------------------------------------------\n   \t\t\t\t -----The first trial-----"

print "---------------------------------------------------------------------------------"

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

# Storing the dimensions of the grid
x = len(grid) - 1
y = len(grid[0]) - 1

# Finding the location of the Starting point
for i in range(x+1):
    for j in range(y+1):
        if grid[i][j] == 0:
            s = [[i, j, 0, 0]]
            break

# Building a tree-like array to keep track of all the paths explored
def add_to_path(i, j, ip, jp, paths):
    for path in paths:
        if path[-1][0] == ip and path[-1][1] == jp:
            break
    path1 = copy.deepcopy(path)
    path1.append([i,j])
    paths.append(path1)
    return paths

def check(i, j, traversed): # To check if a certain pair of indices exists in the traversed list
    for node in traversed:
        if node[0] == i and node[1] == j:
            return True
    return False

# Given a block, this function returns all possible neighbours and their cost
def neighbours(i,j):
    n = []
    # Checking for the right neighbour
    if j < y:
        if grid[i][j+1] != -1:
            n.append([i,j+1 , grid[i][j+1]])
    
    # Checking for the left neighbour
    if j > 0:
        if grid[i][j-1] != -1:
            n.append([i, j-1, grid[i][j-1]])
    
    # Checking for the upper neighbour
    if i > 0:
        if grid[i-1][j] != -1:
            n.append([i-1, j, grid[i-1][j]])
    
    # Checking for the lower neighbour
    if i < x:
        if grid[i+1][j] != -1:
            n.append([i+1, j, grid[i+1][j]])
    return n


def UCS(frontiers, traversed, paths): # The Unifor Cost Search functions
    for node in neighbours(traversed[-1][0], traversed[-1][1]):
        if check(node[0], node[1], traversed) == False:
            if node[2] == 9: # If the value of the cell is 9 it means that we've reached to the goal
                add_to_path(node[0], node[1], traversed[-1][0], traversed[-1][1], paths)
                for path in paths:
                    if path[-1][0] == node[0] and path[-1][1] == node[1]:
                        break
                
                # Printing the original board
                print "The original board:\n"
                for row in grid:
                    for val in row:
                        print '{:4}'.format(val),
                    print 
                print
                print "The algorithm used here is the Uniform Cost Search.\n"
                print "No heuristics is used for UCS.\n"
                temp = []
                temp = [node[0], node[1], grid[node[0]][node[1]], traversed[-1][3]]
                traversed.append(temp)
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
                print "Solution length:", traversed[-1][3]
                print                 
                print "The solution path which starts from 0 and ends in {} which is the goal location:\n".format(number-1)
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
                temp = []
                temp = [node[0], node[1], node[2] + traversed[-1][3], traversed[-1][0], traversed[-1][1]]
                if temp not in frontiers:
                    frontiers.append(temp)
    f = 1
    numbers = []
    for f in frontiers:
            numbers.append(f[2]) 
    mi = min(numbers)
    for f in frontiers:
        if f[2] == mi:
            frontier = f
            break

    frontiers.remove(frontier)
    temp = [frontier[0], frontier[1], grid[frontier[0]][frontier[0]], frontier[2]]
    traversed.append(temp)
    
    UCS(frontiers, traversed, paths)  
    
UCS([], s, [[[s[0][0], s[0][1]]]])
print 
print "---------------------------------------------------------------------------------\n   \t\t\t\t -----The second trial-----"

print "---------------------------------------------------------------------------------"

# Having another grid for the second trial
grid = [
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


# Finding the location of the Starting point
for i in range(x+1):
    for j in range(y+1):
        if grid[i][j] == 0:
            s = [[i, j, 0, 0]]
            break
        
UCS([], s, [[[s[0][0], s[0][1]]]])
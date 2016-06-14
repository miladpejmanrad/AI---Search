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
            s = [[i, j, 0]]
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
    
# Given a cell, this function returns all possible neighbours and their costs
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

f = 0
def BFS(nodes, traversed, paths):
    #print "paths:", paths
    #print
    next_layer = []
    for node in nodes:
        if node[2] == 9:
            add_to_path(node[0], node[1], traversed[-1][0], traversed[-1][1], paths)
            for path in paths:
                if path[-1][0] == node[0] and path[-1][1] == node[1]:
                    break
            traversed.append(node)
            f = 1 # When we reach the goal, we change the flag to 1 so that it does the final step 
            break

        traversed.append(node)
        for n in neighbours(node[0],node[1]):
            if n not in traversed and n not in next_layer:
                next_layer.append(n)
                add_to_path(n[0], n[1], node[0], node[1], paths)
                
    try:
        if f == 1:
            
            # Printing the original board
            print "The original board:\n"
            for row in grid:
                for val in row:
                    print '{:4}'.format(val),

                print 
            print
            print "The algorithm used here is Breadth First Search.\n"
            print "No heuristics is used for BFS.\n"
            grid_changed = copy.deepcopy(grid)
            for i in range(x+1):
                for j in range(y+1):
                    if [i, j] not in path:
                        grid_changed[i][j] = -1
                        
            number = 0
            solution_length = 0
            for node in path:
                solution_length = solution_length + grid[node[0]][node[1]]
                grid_changed[node[0]][node[1]] = number
                number += 1
            
            print "Number of nodes explored:", len(path)
            print
            print "Solution length:", solution_length-9
            print 
            print "The solution path which starts from 0 and ends in {} which is the goal location:\n".format(number-1)
            for row in grid_changed:
                for val in row:
                    if val != -1:
                        print '{:4}'.format(val),
                    else:
                        print '{:4}'.format(""),
                print
        print 
    except:

        BFS(next_layer, traversed, paths)

BFS(s, [], [[[s[0][0], s[0][1]]]])  
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
            s = [[i, j, 0]]
            break

BFS(s, [], [[[s[0][0], s[0][1]]]]) 
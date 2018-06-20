#Function getGrid takes size argumentand ruturns a grid with provided size

def getGrid(size):
    matrix = []
    for i in range(0, size):
        matrix.append([])
        for j in range(0, size):
            matrix[i].append(" ")
    return matrix

# printGrid takes a grid argument and prints it formatted on a screen

def printGrid(grid):
    for i in range(0, len(grid)):
        for j in range(0, len(grid)):
            if j == len(grid) - 1:
                print(grid[i][j])
            else:
                print(grid[i][j] + " | ", end='')
        if not i == len(grid) - 1:
            for k in range(0, len(grid)):
                print('---', end='')
            print('--')

# rotateGrid takes a grid as an argument and returns another grid that is rotated 
# (so horizontal lines are vertical)

def rotateGrid(grid):
    grid2 = getGrid(len(grid))

    for i in range(len(grid2)):
        for j in range(len(grid2[i])):
            grid2[i][j] = grid[j][i]

    return grid2
import gridgen
import random

# Functions that takes player input and adds a symbol on a map via provided input 
def gridFill(grid,g, size):

    while g<size:
        l=['A','B','C', 'D', 'E']
        n=['1','2','3', '4', '5']
        grid[0][g]=n[g-1]
        grid[g][0]=n[g-1]
        g=g+1



def plrChoose(grid, whichOne, plr):
    if whichOne == True:
        usr = input("P1: Choose an empty spot(xy): ")
        if (usr.isdigit()== True 
            and 1<=int(usr[0])<4 
            and 1<=int(usr[1])<4 
            and len(usr)==2):
            
            x = int(usr[1])
            y = int(usr[0])
            if grid[x][y] == " ":
                grid[x][y] = "x"
                if plr == '2':
                    return False
                else:
                    return None
            else:
                print("That spot is already taken!")
        else:
            print("Wrong imput. Try again!")
            return True
    if whichOne == False:
        usr = input("P2: Choose an empty spot(xy): ")
        if usr.isdigit()== True and 0<int(usr[0])<4 and 0<int(usr[1])<4 and len(usr)==2:
            x = int(usr[1])
            y = int(usr[0])
            if grid[x][y] == " ":
                grid[x][y] = "o"
                return True
            else:
                print("That spot is already taken!")
        else: print("Wrong imput. Try again!")
    else:
        x = random.randint(1,3)
        y = random.randint(1,3)
        if grid[x][y] ==" ":
            grid[x][y] = "o"
            return True

# Function that checks grid for a winner

def checkGrid(grid):
    ln = len(grid)   # Variable to store the length of the grid
    rotGrid = gridgen.rotateGrid(grid) # Preparing the rotated grid, to check on the vertical lines
    for j in range(ln):
        if grid[j].count("x") == ln-1:  # Here, the function checks the lines, first horizontal, then the vertical, each for both players
            print("Player 1 wins! 1")
            return True
        elif grid[j].count("o") == ln-1:
            print("Player 2 wins! 2")
            return True
        elif rotGrid[j].count("x") == ln-1:
            print("Player 1 wins! 3")
            return True
        elif rotGrid[j].count("o") == ln-1:
            print("Player 2 wins! 4" )
            return True
    # Here the function is checking the diagonal-possibilities. Its ugly as hell, i know :<
    if grid[3][3] == 'x' and grid[1][1] == 'x' and grid[2][2] == 'x':
        print("Player 1 wins! 5")
        return True
    elif grid[3][1] == 'x' and grid[2][2] == 'x' and grid[1][3] == 'x':
        print("Player 1 wins! 6")
        return True
    elif grid[3][3] == 'o' and grid[1][1] == 'o' and grid[2][2] == 'o':
        print("Player 2 wins! 7")
        return True
    elif grid[3][1] == 'o' and grid[2][2] == 'o' and grid[1][3] == 'o':
        print("Player 2 wins! 8")
        return True
    return False

def movesLeft(grid):
    emptySpots = 0
    for i in grid:
        for j in i:
            if j == " ":
                emptySpots += 1
    if emptySpots==1:
        print("Draw! No one wins!")
        return True
    return False
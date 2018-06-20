import gridgen
import userinput

# Imported modules are selfmade files with definitions of functions 
# that are running the game

# Setup:
# gameOver is a boolean telling the program when to end the game;
# player is a boolean that represents which player should move now: True is P1 and False is P2
# (by deafaut P1 starts)
# size is value of the side of the grid
# time is a variable that keeps track of used moves
# the game is caled a draw, when all the possible moves are done
plr = input("If you wana play with friend press 2. if you want to play with computer press 1. : ")


gameOver = False
player = True
size = 4
g = 1


if plr == '2' or plr == '1':

    newGrid = gridgen.getGrid(int(size))
    userinput.gridFill(newGrid, g, size,)
    gridgen.printGrid(newGrid)
    while not gameOver:
        player = userinput.plrChoose(newGrid, player,plr)
        gridgen.printGrid(newGrid)
        if gameOver == False:
            gameOver = userinput.checkGrid(newGrid)
        if gameOver == False:
            gameOver = userinput.movesLeft(newGrid)
    print("G A M E  O V E R")
else:
    plr = input('nope thats not a right number. please try again')

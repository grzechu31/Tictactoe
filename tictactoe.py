import gridgen
import userinput
import midi_display

# Imported modules are selfmade files with definitions of functions 
# that are running the game

# Setup:
# gameOver is a boolean telling the program when to end the game;
# player is a boolean that represents which player should move now: True is P1 and False is P2
# (by deafaut P1 starts)
# size is value of the side of the grid
# time is a variable that keeps track of used moves
# the game is caled a draw, when all the possible moves are done

def main(port=midi_display.default_setup()):
    print("Welcome to TicTacToe in python!")
    print("Choose an option:\n")
    print("1. Player vs A.I.")
    print("2. Player vs Player")
    print("3. Midi setup\n")
    print("4. Quit\n")
    choice = input(">>")
    while not choice.isdigit() or not int(choice) in range(1,5):
        print("Wrong input, try again.")
        choice = input(">>")
    choice = int(choice)
    if choice == 4:
        pass
    elif choice == 3:
        port = midi_display.setup()
        main(port)
    else:
        launch_game(choice, port)

def launch_game(plr, port=midi_display.default_setup()):
    gameOver = False
    player = True
    size = 4
    g = 1


    newGrid = gridgen.getGrid(int(size))
    userinput.gridFill(newGrid, g, size,)
    gridgen.printGrid(newGrid)
    midi_display.showGrid(newGrid, port)
    while not gameOver:
        player = userinput.plrChoose(newGrid, player,plr)
        gridgen.printGrid(newGrid)
        midi_display.showGrid(newGrid, port)
        if gameOver == False:
            gameOver = userinput.checkGrid(newGrid)
        if gameOver == False:
            gameOver = userinput.movesLeft(newGrid)
    print("G A M E  O V E R")
    midi_display.clear(port)

if __name__ == "__main__":
    main()

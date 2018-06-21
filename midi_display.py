import rtmidi
import time

# This default function is called to set a harmless midi_port.

def default_setup():
    mo = rtmidi.MidiOut()
    midi_port = mo.open_port(0)
    return (midi_port, 0)

# setup function is for choosing the correct midi port, for controling the launchpad

def setup():
    mo = rtmidi.MidiOut()
    ports_list = mo.get_ports()
    print("These are your midi ports:\n")
    for port in ports_list:
        print("{}: {}".format(ports_list.index(port), port))
    print("\nYou should be looking for ports named 'Launchpad Pro' or 'Launchpad Mini'.")
    port_no = input("Choose port number to use:")
    while not port_no.isdigit() or not int(port_no) in range(len(ports_list)):
        print("Wrong input, try again.")
        port_no = input("Choose port number to use:")
    midi_port = mo.open_port(int(port_no))
    print("Opened port: ", port_no)
    return (midi_port, int(port_no))

    
def clear(midi_port_list):
    midi_port = midi_port_list[0]
    port_name = midi_port_list[0].get_port_name(midi_port_list[1])
    if port_name.find("Launchpad Mini") > -1:
        midi_port.send_message([0x90, 176, 0, 0])
    if port_name.find("Launchpad Pro") > -1:
        midi_port.send_message([240,0,32,41,2,16,14,0,247])
# Main function for displaying the grid on the Launchpad 

def launchpad_mini(grid, midi_port_list):
    midi_port = midi_port_list[0]
    core_list = [0,1,16,17]
    for i in range(2, 115,16):
        midi_port.send_message([0x90, i, 29]) # 7 and 28 are position and color, taken from the docs

    for i in range(5, 118,16):
        midi_port.send_message([0x90, i, 29])

    for i in range(32, 40):
        midi_port.send_message([0x90, i, 29])

    for i in range(80, 88):
        midi_port.send_message([0x90, i, 29])

    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            coordinate = (i - 1) * 48
            coordinate += (j - 1) * 3
            final_list = []
            for val in core_list:
                val += coordinate
                final_list.append(val)
            if grid[i][j] == 'x':
                for val in final_list:
                    midi_port.send_message([0x90, val, 11])
            if grid[i][j] == 'o':
                for val in final_list:
                    midi_port.send_message([0x90, val, 56])

def launchpad_pro(grid, midi_port_list):
    core_list = [81,82,91,92]
    midi_port = midi_port_list[0]

    for i in range(83, 14, -10):
        midi_port.send_message([240,0,32,41,2,16,10,i, 3, 247])
    for i in range(61, 69):
        midi_port.send_message([240,0,32,41,2,16,10,i, 3, 247])
    for i in range(86, 17, -10):
        midi_port.send_message([240,0,32,41,2,16,10,i, 3, 247])
    for i in range(31, 39):
        midi_port.send_message([240,0,32,41,2,16,10,i, 3, 247])

    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            coordinate = (i) * 30
            coordinate += (j) * 3
            final_list = []
            for val in core_list:
                val -= coordinate
                final_list.append(val)
            if grid[i][j] == 'x':
                for val in final_list:
                    midi_port.send_message([240,0,32,41,2,16,10,val, 72, 247])
            if grid[i][j] == 'o':
                for val in final_list:
                    midi_port.send_message([240,0,32,41,2,16,10,val, 67, 247])

def showGrid(grid, midi_port_list):
    clear(midi_port_list)
    port_name = midi_port_list[0].get_port_name(midi_port_list[1])
    if port_name.find("Launchpad Mini") > -1:
        launchpad_mini(grid, midi_port_list)
    if port_name.find("Launchpad Pro") > -1:
        launchpad_pro(grid, midi_port_list)  

def game_over(grid, midi_port_list):
    core_list = [0,1,16,17]
    midi_port = midi_port_list[0]
    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            coordinate = (i - 1) * 48
            coordinate += (j - 1) * 3
            final_list = []
            for val in core_list:
                val += coordinate
                final_list.append(val)
            if grid[i][j] == 'x':
                for val in final_list:
                    midi_port.send_message([0x90, val, 11])
            if grid[i][j] == 'o':
                for val in final_list:
                    midi_port.send_message([0x90, val, 56])
    time.sleep(1)
    for i in range(1, len(grid)):
        for j in range(1, len(grid)):
            coordinate = (i - 1) * 48
            coordinate += (j - 1) * 3
            final_list = []
            for val in core_list:
                val += coordinate
                final_list.append(val)
            if grid[i][j] == 'x':
                for val in final_list:
                    midi_port.send_message([0x90, val, 0])
            if grid[i][j] == 'o':
                for val in final_list:
                    midi_port.send_message([0x90, val, 0])

    time.sleep(1)


""" while True:
    x = input("str ")
    if x == 'q':
        break
    x1 = int(x[0])
    x2 = int(x[1])
    coordinate = (x1 - 1) * 48
    coordinate += (x2 - 1) * 3

    core_list = [0,1,16,17]
    final_list = []
    for val in core_list:
        val += coordinate
        final_list.append(val)

    for val in final_list:
        midi_port.send_message([0x90, val, 11])

midi_port.send_message([0x90, 176, 0, 0])
 """


# def showGrid(grid):

# light up the top-right pad with green color 
# midi_port.send_message([0x90, 12, 60]) # 7 and 28 are position and color, taken from the docs
# midi_port.send_message([240,0,32,41,2,16,10,12,0,247])
# mo.close_port()
# del mo
# docs: https://global.novationmusic.com/support/downloads/launchpad-programmers-reference-guide
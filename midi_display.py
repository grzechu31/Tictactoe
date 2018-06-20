import rtmidi

# setup function is for choosing the correct midi port, for controling the launchpad
def default_setup():
    mo = rtmidi.MidiOut()
    midi_port = mo.open_port(0)
    return midi_port
    
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
    return midi_port
    
def clear(midi_port):
    midi_port.send_message([0x90, 176, 0, 0])


def showGrid(grid, midi_port):
    global core_list
    clear(midi_port)
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



core_list = [0,1,16,17]

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
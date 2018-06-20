import rtmidi

mo = rtmidi.MidiOut()
for port_no in range(mo.get_port_count()):
    port_name = mo.get_port_name(port_no)
    if port_name.find('Launchpad Mini') > -1:
        mo.close_port()
        midi_port = mo.open_port(port_no)
        print("Using: ", port_name)
        break
    elif port_name.find('Launchpad Pro:Launchpad Pro MIDI 2') > -1:
        mo.close_port()
        midi_port = mo.open_port(port_no)
        print("Using: ", port_name)
        break
        
midi_port.send_message([0x90, 176, 0, 0])

for i in range(2, 115,16):
    midi_port.send_message([0x90, i, 29]) # 7 and 28 are position and color, taken from the docs

for i in range(5, 118,16):
    midi_port.send_message([0x90, i, 29])

for i in range(32, 40):
    midi_port.send_message([0x90, i, 29])

for i in range(80, 88):
    midi_port.send_message([0x90, i, 29])


while True:
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



# def showGrid(grid):

# light up the top-right pad with green color 
# midi_port.send_message([0x90, 12, 60]) # 7 and 28 are position and color, taken from the docs
# midi_port.send_message([240,0,32,41,2,16,10,12,0,247])
# mo.close_port()
# del mo
# docs: https://global.novationmusic.com/support/downloads/launchpad-programmers-reference-guide
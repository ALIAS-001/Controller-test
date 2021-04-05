import inputs as inp
import curses 
#set up the dictionaries needed for conversion
Key = [0,0,0,0,0,0,0,0,0,0]
Abs = [0,0,0,0,0,0,0,0]
Key_Dict = {
    "BTN_START" : 1,    #Start
    "BTN_SELECT" : 0,   #Select
    "BTN_TL" : 2,       #Left trigger
    "BTN_TR" : 3,       #Right trigger
    "BTN_SOUTH" : 4,    #A
    "BTN_EAST" : 5,     #B
    "BTN_WEST" : 6,     #X
    "BTN_NORTH" : 7,    #Y
    "BTN_THUMBL" : 8,   #Left Stick Button
    "BTN_THUMBR" : 9    #Right Stick Button
}
Abs_Dict = {
    #D-pad
    "ABS_HAT0X" : 0,
    "ABS_HAT0Y" : 1,
    #Left stick
    "ABS_X": 2,
    "ABS_Y" : 3,
    #Right Stick
    "ABS_RX" : 4,
    "ABS_RY" : 5,
    #Left trigger
    "ABS_Z" : 6,
    #right trigger
    "ABS_RZ" : 7
}
#curses
#custom output for a nintendo switch pro controler (PC indicates a XBOX 360 controlller)
#Differences, A and X buttons are Mirrored as well as the B and Y
#Had to fiddle with the spacing for the output to make it look nice
def output(stdscr):
    stdscr.addstr(0,0,"Press Start and Select at the same time to exit")
    stdscr.addstr(1,0,f'    left trigger: {Abs[6]:^3}      right trigger: {Abs[7]:^3}')
    stdscr.addstr(2,0,f'    left bumper: {Key[2]}         right bumper: {Key[3]}')
    stdscr.addstr(3,0,f'left stick      Select	Start           X: {Key[6]}	')
    stdscr.addstr(4,0,f'X: {Abs[2]:^6}          {Key[1]}       {Key[0]}	    Y: {Key[7]}    A: {Key[4]}')
    stdscr.addstr(5,0,f'Y: {Abs[3]:^6}              Right Stick      B: {Key[5]}')
    stdscr.addstr(6,0,f'Button:	{Key[8]}                X: {Abs[4]:^6}')
    stdscr.addstr(7,0,f'        D-Pad            Y: {Abs[5]:^6}')
    stdscr.addstr(8,0,f'        X: {Abs[0]:^2} Y: {Abs[1]:^2}      Button: {Key[9]}')
def main(stdscr):
    '''
    stdscr.addstr(0,0,f'Start: {Key[0]}, Select: {Key[1]}, Left Tirgger: {Key[2]}, Right Trigger: {Key[3]}, A: {Key[4]}, B: {Key[5]}, X: {Key[6]}, Y: {Key[7]}, Left Button: {Key[8]}, Right Button Button: {Key[9]}')
    stdscr.addstr(1,0,f'Left stick[X: {Abs[2]:^6} Y: {Abs[3]:^6} ], Right Stick[X: {Abs[4]:^6} Y:{Abs[5]:^6} ], D-pad[X: {Abs[0]:^2} Y {Abs[1]:^2} ], Left trigger: {Abs[6]:^3}, Right trigger{Abs[7]:^3}')
    stdscr.addstr(2,0,"Press Start and Select to return")
    '''    
    output(stdscr)
    stdscr.refresh()
    while 1:
        events = inp.get_gamepad()      #get inputs from the connected gamepad
        for event in events:
            if event.ev_type != "Sync":
    
                if event.ev_type == "Key":
                    Key[Key_Dict[event.code]] = event.state
                elif event.ev_type == "Absolute":
                    Abs[Abs_Dict[event.code]] = event.state
                '''
                #Key output
                stdscr.addstr(0,0,f'Start: {Key[0]}, Select: {Key[1]}, Left Tirgger: {Key[2]}, Right Trigger: {Key[3]}, A: {Key[4]}, B: {Key[5]}, X: {Key[6]}, Y: {Key[7]}, Left Button: {Key[8]}, Right Button Button: {Key[9]}')
                #ABS output
                stdscr.addstr(1,0,f'Left stick[X: {Abs[2]:^6} Y: {Abs[3]:^6} ], Right Stick[X: {Abs[4]:^6} Y:{Abs[5]:^6} ], D-pad[X: {Abs[0]:^2} Y {Abs[1]:^2} ], Left trigger: {Abs[6]:^3}, Right trigger{Abs[7]:^3}')
                '''
                output(stdscr)
                
                stdscr.refresh()
                if Key[0] == 1 and Key[1] == 1:
                    return
    '''
    for event in events:
        #print(event.code)
        if event.ev_type != "Sync":
            if event.ev_type == "Key":
                if event.code == "BTN_START":
                    print("Start",end=' ')
                if event.code == "BTN_SELECT":
                    print("Select",end=' ')
                if event.code == "BTN_TL":
                    print("Left bumper",end=' ')
                if event.code == "BTN_TR":
                    print("Right bumper",end=' ')
                if event.code == "BTN_SOUTH":
                    print("A",end=' ')
                if event.code == "BTN_EAST":
                    print("B",end=' ')
                if event.code == "BTN_WEST":
                    print("X",end=' ')
                if event.code == "BTN_NORTH":
                    print("Y",end=' ')
                if event.code == "BTN_THUMBL":
                    print("Left Stick Button",end=' ')
                if event.code == "BTN_THUMBR":
                    print("Right Stick Button",end=' ')
            if event.ev_type == "Absolute":
                if event.code == "ABS_HAT0X" or event.code == "ABS_HAT0Y":
                    print("D-pad",end=' ')
                if event.code == "ABS_X" or event.code == "ABS_Y":
                    print("Left Stick",end=' ')
                if event.code == "ABS_RX" or event.code == "ABS_RY":
                    print("Right Stick",end=' ')
                if event.code == "ABS_Z":
                    print("Left trigger",end=' ')
                if event.code == "ABS_RZ":
                    print("Right trigger",end=' ')
            print(event.state,end='\r')'''
'''
console = curses.initscr()
console.clear()
'''
try:
    curses.wrapper(main)
except (KeyboardInterrupt, SystemExit):
    pass


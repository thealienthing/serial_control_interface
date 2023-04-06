from serial import Serial
from sys import argv
from basics import basics_tab, OSC1_GROUP, OSC2_GROUP
from waveshaping import waveshaping_tab
import PySimpleGUI as sg
from events import Event
import time

tabs = sg.TabGroup([[basics_tab, waveshaping_tab]])

window = sg.Window("Shiny OctoTrain Control App", [[tabs]])
#con = Serial(argv[1], 115200)
settings = {}

while True:
    event, values = window.read()
    
    print("Event: ", event, "Value: ", values[event])
    
    if event == sg.WIN_CLOSED:
        break

    # window.refresh()

window.close()



from serial import Serial
from sys import argv
from basics import basics_tab, OSC1_GROUP, OSC2_GROUP
from waveshaping import waveshaping_tab
import PySimpleGUI as sg
from events import Event
import json
import time
from patches import patch, patches_tab

tabs = sg.TabGroup([[basics_tab, waveshaping_tab, patches_tab]])


window = sg.Window("Shiny OctoTrain Control App", [[tabs]])
con = Serial(argv[1], 115200)
patch.set_serial_con(con)

while True:
    try:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED:
            print("Closing window")
            break
        
        if event is Event.DUMP_PATCH_DATA:
            patch.save()
            continue

        if event is Event.PATCH_NAME:
            patch.name = values[event]
            continue

        if event is Event.LOAD_PATCH:
            patch.load()

        if event is Event.SELECT_PATCH:
            patch.select(values[event][0])

        if event in values:
            patch.add_event_data(event, values[event])

        # window.refresh()
    except Exception as err:
        if window is None:
            print("Window is none")
        print(f"Error occured: {err}")

window.close()



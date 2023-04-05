from serial import Serial
from sys import argv
from basics import basics_tab
from waveshaping import waveshaping_tab
import PySimpleGUI as sg
import time


tabs = sg.TabGroup([[basics_tab, waveshaping_tab]])

window = sg.Window("Shiny OctoTrain Control App", [[tabs]])
#con = Serial(argv[1], 115200)

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break

    # window.refresh()

window.close()



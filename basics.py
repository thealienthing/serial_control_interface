import PySimpleGUI as sg
from events import Event

OSC1_GROUP = "OSC1_GROUP"
OSC2_GROUP = "OSC2_GROUP"

osc1_layout = sg.Frame("Osc1", [
    [sg.Radio("Sin", OSC1_GROUP, key=Event.OSC1_SIN, enable_events=True)],
    [sg.Radio("Saw", OSC1_GROUP, key=Event.OSC1_SAW, enable_events=True)],
    [sg.Radio("Square", OSC1_GROUP, key=Event.OSC1_SQUARE, enable_events=True)],
    [sg.Radio("Triangle", OSC1_GROUP, key=Event.OSC1_TRI, enable_events=True)],
    [sg.Radio("Noise", OSC1_GROUP, key=Event.OSC1_NOISE, enable_events=True)]
])

osc2_layout = sg.Frame("Osc2", [
    [sg.Radio("Sin", OSC2_GROUP, key=Event.OSC2_SIN, enable_events=True)],
    [sg.Radio("Saw", OSC2_GROUP, key=Event.OSC2_SAW, enable_events=True)],
    [sg.Radio("Square", OSC2_GROUP, key=Event.OSC2_SQUARE, enable_events=True)],
    [sg.Radio("Triangle", OSC2_GROUP, key=Event.OSC2_TRI, enable_events=True)],
    [sg.Radio("Noise", OSC2_GROUP, key=Event.OSC2_NOISE, enable_events=True)]
])

mixer_layout = sg.Frame("Oscillator Mix", [
    [
        sg.Text("Osc1 Gain"),
        sg.Text("Osc2 Gain")
    ],
    [
        sg.Slider(range=(0.0, 1.0), resolution=0.01, orientation='v', default_value=0.5, key=Event.OSC1_GAIN, enable_events=True),
        sg.Slider(range=(0.0, 1.0), resolution=0.01, orientation='v', default_value=0.5, key=Event.OSC2_GAIN, enable_events=True)
    ]
])

basics_layout = [[
    sg.Col([
        [sg.Text("Oscillators")],
        [osc1_layout, osc2_layout],
        [
            sg.Text('Osc2 Semitone'), 
            sg.Spin([i for i in range(-24,24)],initial_value=0, size=(6,1), key=Event.OSC2_SEMITONE, enable_events=True)
        ],
        [
            sg.Text('Osc2 Tune(hz)'), 
            sg.Spin([i for i in range(-50,50)], initial_value=0, size=(6,1), key=Event.OSC2_TUNE, enable_events=True)
        ]
    ]),
    sg.Col([
        [mixer_layout]
    ])
]]

basics_tab = sg.Tab("Basics", basics_layout)
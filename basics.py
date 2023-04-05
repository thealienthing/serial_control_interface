import PySimpleGUI as sg

OSC1_GROUP = "OSC1_GROUP"
OSC2_GROUP = "OSC2_GROUP"

osc1_layout = sg.Frame("Osc1", [
    [sg.Radio("Sin", OSC1_GROUP)],
    [sg.Radio("Saw", OSC1_GROUP)],
    [sg.Radio("Square", OSC1_GROUP)],
    [sg.Radio("Triangle", OSC1_GROUP)],
    [sg.Radio("Noise", OSC1_GROUP)]
])

osc2_layout = sg.Frame("Osc2", [
    [sg.Radio("Saw", OSC2_GROUP)],
    [sg.Radio("Sin", OSC2_GROUP)],
    [sg.Radio("Square", OSC2_GROUP)],
    [sg.Radio("Triangle", OSC2_GROUP)],
    [sg.Radio("Noise", OSC2_GROUP)]
])

mixer_layout = sg.Frame("Oscillator Mix", [
    [
        sg.Text("Osc1 Gain"),
        sg.Text("Osc1 Gain")
    ],
    [
        sg.Slider(range=(0.0, 1.0), resolution=0.01, orientation='v', default_value=0.5),
        sg.Slider(range=(0.0, 1.0), resolution=0.01, orientation='v', default_value=0.5)
    ]
])

basics_layout = [[
    sg.Col([
        [sg.Text("Oscillators")],
        [osc1_layout, osc2_layout],
        [sg.Text('Osc2 Semitone'), sg.Spin([i for i in range(-24,24)], initial_value=0, size=(6,1))],
        [sg.Text('Osc2 Tune(hz)'), sg.Spin([i for i in range(-50,50)], initial_value=0, size=(6,1))]
    ]),
    sg.Col([
        [mixer_layout]
    ])
]]

basics_tab = sg.Tab("Basics", basics_layout)
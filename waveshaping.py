import PySimpleGUI as sg
from combined_elemnts import labeled_vertical_slider

FILTER_GROUP = "FILTER_GROUP"

amp_env_layout = sg.Frame("Amp Envelope", [
    [
        sg.Col(labeled_vertical_slider("A", "", (5, 5000), 1)),
        sg.Col(labeled_vertical_slider("D", "", (0.1, 1.0), 0.01)),
        sg.Col(labeled_vertical_slider("S", "", (5, 5000), 1)),
        sg.Col(labeled_vertical_slider("R", "", (5, 5000), 1))
    ]
])

filter_env_layout = sg.Frame("Filter Envelope", [
    [
        sg.Col(labeled_vertical_slider("A", "", (5, 5000), 1)),
        sg.Col(labeled_vertical_slider("D", "", (0.1, 1.0), 0.01)),
        sg.Col(labeled_vertical_slider("S", "", (5, 5000), 1)),
        sg.Col(labeled_vertical_slider("R", "", (5, 5000), 1))
    ]
])

filter_layout = sg.Frame("Filter", [
    [sg.Radio("Low Pass", FILTER_GROUP)],
    [sg.Radio("High Pass", FILTER_GROUP)],
    [
        sg.Col(labeled_vertical_slider("Cutoff", "", (5, 2000), 1, 200)),
        sg.Col(labeled_vertical_slider("Resolution", "", (1.0, 8.0), 0.1, 1.0)),
        sg.Col(labeled_vertical_slider("Filter Env", "", (0.1, 1.0), 0.01, 1.0)),
    ]
])

waveshaping_layout = [
    [
        amp_env_layout,
        filter_env_layout,
        filter_layout
    ]
]

waveshaping_tab = sg.Tab("Waveshaping", waveshaping_layout)
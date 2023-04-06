import PySimpleGUI as sg
from events import Event
from combined_elemnts import labeled_vertical_slider

FILTER_GROUP = "FILTER_GROUP"

amp_env_layout = sg.Frame("Amp Envelope", [
    [
        sg.Col(labeled_vertical_slider("A", Event.AMP_ENV_ATTACK, (5, 5000), 1)),
        sg.Col(labeled_vertical_slider("D", Event.AMP_ENV_DECAY, (0.1, 1.0), 0.01)),
        sg.Col(labeled_vertical_slider("S", Event.AMP_ENV_SUSTAIN, (5, 5000), 1)),
        sg.Col(labeled_vertical_slider("R", Event.AMP_ENV_RELEASE, (5, 5000), 1))
    ]
])

filter_env_layout = sg.Frame("Filter Envelope", [
    [
        sg.Col(labeled_vertical_slider("A", Event.FILTER_ENV_ATTACK, (5, 5000), 1)),
        sg.Col(labeled_vertical_slider("D", Event.FILTER_ENV_DECAY, (0.1, 1.0), 0.01)),
        sg.Col(labeled_vertical_slider("S", Event.FILTER_ENV_SUSTAIN, (5, 5000), 1)),
        sg.Col(labeled_vertical_slider("R", Event.FILTER_ENV_RELEASE, (5, 5000), 1))
    ]
])

filter_layout = sg.Frame("Filter", [
    [sg.Radio("Low Pass", FILTER_GROUP, key=Event.FILTER_LOWPASS, enable_events=True)],
    [sg.Radio("High Pass", FILTER_GROUP, key=Event.FILTER_HIGHPASS, enable_events=True)],
    [
        sg.Col(labeled_vertical_slider("Cutoff", Event.FILTER_CUTOFF, (5, 20000), 1, 200)),
        sg.Col(labeled_vertical_slider("Resonance", Event.FILTER_RESONANCE, (1.0, 8.0), 0.1, 1.0)),
        sg.Col(labeled_vertical_slider("Filter Env", Event.FILTER_ENV_INTENSITY, (0.1, 1.0), 0.01, 1.0)),
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
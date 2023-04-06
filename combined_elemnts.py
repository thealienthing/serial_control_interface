import PySimpleGUI as sg

def labeled_vertical_slider(label, key, range, resolution, default=None):
    return [
        [sg.Text(label, justification='center')],
        [sg.Slider(range=range, resolution=resolution, orientation='vertical',
            size=(10, 20), key=key, default_value=default, disable_number_display=True, enable_events=True)
        ]
    ]
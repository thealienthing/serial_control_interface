import PySimpleGUI as sg
import json
import os
import struct
from serial import Serial
from events import Event
from enum import Enum

PATCH_SAVE_FILE = "patches.json"
PARAM_HEADER = 0xDEADBEEF

class Patch:
    def __init__(self,):
        self.serial_con = None
        self.patch_data = {}
        self.bank_names = []
        self.name = ""
        self.selected_patch = ""
        #If a patch file does not exist, make an empty one
        if not os.path.exists(PATCH_SAVE_FILE):
            f = open(PATCH_SAVE_FILE, "w")
            json.dump(self.patch_data, f)
            f.close()
        else:
            f = open(PATCH_SAVE_FILE, "r")
            patch_bank = json.load(f)
            for key in patch_bank:
                self.bank_names.append(key)
            f.close()

    def add_event_data(self, event: Event, value):
        if "OSC1_WAVEFORM" in event.name:
            for key in self.patch_data:
                if "OSC1_WAVEFORM" in key:
                    del self.patch_data[key]
                    break

        if "OSC2_WAVEFORM" in event.name:
            for key in self.patch_data:
                if "OSC2_WAVEFORM" in key:
                    del self.patch_data[key]
                    break

        self.send_serialized_data(event.value, value)
        self.patch_data[event.name] = [event.value, value]

    def save(self):
        if self.name:
            with open(PATCH_SAVE_FILE, "r") as f:
                patch_list = json.load(f)
            patch_list[self.name] = self.patch_data
            print(json.dumps(patch_list, indent=4))
            f = open(PATCH_SAVE_FILE, "w")
            json.dump(patch_list, f, indent=4)
            f.close()
        else:
            print("No patch name")

    def select(self, name):
        self.selected_patch = name
        print("Select patch: ", self.selected_patch)

    def load(self):
        print("Load patch: ", self.selected_patch)
        with open(PATCH_SAVE_FILE, "r") as f:
            patch_list = json.load(f)
            self.patch_data = patch_list[self.selected_patch]
        print(json.dumps(self.patch_data, indent=4))

    def send_serialized_data(self, data_key, val):
        header = struct.pack("<I", PARAM_HEADER)
        data_key = struct.pack("<I", data_key)
        val = struct.pack("<f", val)
        serialized_data = header + data_key + val
        print(serialized_data)
        if self.serial_con:
            self.serial_con.write(serialized_data)
        #print(f"Sending data key {struct.unpack('<I', data_key)} with val {struct.unpack('<f', val)}")

    def set_serial_con(self, serial_con):
        self.serial_con = serial_con

patch = Patch()

patches_layout = [[
        sg.Col([
            [sg.InputText(key=Event.PATCH_NAME, enable_events=True)],
            [sg.Button("Dump Patch Data", key=Event.DUMP_PATCH_DATA)]
        ]),
        sg.Col([
            [sg.Listbox(patch.bank_names, size=(20,10), key=Event.SELECT_PATCH, enable_events=True)],
            [sg.Button("Load patch", key=Event.LOAD_PATCH)]
        ])
]]

patches_tab = sg.Tab("Patches", patches_layout)

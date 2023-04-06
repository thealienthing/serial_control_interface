from events import Event
from serial import Serial

class SynthDataMarshal:
    def __init__(self, serial_fd):
        self.serial_fd = serial_fd
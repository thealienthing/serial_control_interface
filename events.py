import enum

class Event(enum.Enum):
    OSC1_SIN = enum.auto()
    OSC1_SAW = enum.auto()
    OSC1_SQUARE = enum.auto()
    OSC1_TRI = enum.auto()
    OSC1_NOISE = enum.auto()

    OSC2_SIN = enum.auto()
    OSC2_SAW = enum.auto()
    OSC2_SQUARE = enum.auto()
    OSC2_TRI = enum.auto()
    OSC2_NOISE = enum.auto()

    OSC2_SEMITONE = enum.auto()
    OSC2_TUNE = enum.auto()

    OSC1_GAIN = enum.auto()
    OSC2_GAIN = enum.auto()

    AMP_ENV_ATTACK = enum.auto()        
    AMP_ENV_DECAY = enum.auto()
    AMP_ENV_SUSTAIN = enum.auto()
    AMP_ENV_RELEASE = enum.auto()

    FILTER_ENV_ATTACK = enum.auto()
    FILTER_ENV_DECAY = enum.auto()
    FILTER_ENV_SUSTAIN = enum.auto()
    FILTER_ENV_RELEASE = enum.auto()
    
    FILTER_LOWPASS = enum.auto()
    FILTER_HIGHPASS = enum.auto()
    FILTER_CUTOFF = enum.auto()
    FILTER_RESONANCE = enum.auto()
    FILTER_ENV_INTENSITY = enum.auto()



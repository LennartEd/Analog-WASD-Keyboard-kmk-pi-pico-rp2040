print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.modules.tapdance import TapDance
from kmk.extensions.RGB import RGB

from kmk.modules.analog import AnalogKey #handles analoginput


# KEYTBOARD SETUP 
layers = Layers()
keyboard = KMKKeyboard()
encoders = EncoderHandler()
ana = AnalogKey()
#tapdance = TapDance()
#tapdance.tap_time = 250


keyboard.modules = [layers, encoders,ana] #tapdance]

# SWITCH MATRIX 
keyboard.col_pins = (board.GP3, board.GP4, board.GP5, board.GP6)
keyboard.row_pins = (board.GP7, board.GP8, board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# ENCODERS
encoders.pins = ((board.GP2, board.GP1, board.GP0, False), (board.GP10, board.GP11, board.GP12, False),)

# EXTENSIONS 
rgb_ext = RGB(pixel_pin = board.GP13, num_pixels=4, hue_default=100)
keyboard.extensions.append(rgb_ext)
keyboard.debug_enabled = False

#ANALOG 
ana.pins = (board.GP29,board.GP28,board.GP27,board.GP26) #define analog pins

ana.reverse = False #flips direction(standard is: analog value goes down when key pressed) 

# define per layer if keypresses should be Threshhold(0) or Rapid trigger(1) explanation: https://wooting.io/rapid-trigger 
ana.keypType = (1, 0) 

#threshold: when analog value is passed key is pressed 
#rapit: when a certain distance is surpaced key is pressed (the lower the value the faster responce but at a certain point noise can trigger keypress)
    #use the provided "maxChangeInVal.py"+ 300 to find a good rapid trigger value
ana.threshold = (30000,1800) 



___ = KC.TRNS
xxx = KC.NO
LA1 = KC.TG(1)
LA0 = KC.TG(0)

# KEYMAP for normal keys
keyboard.keymap = [
    [
        LA1,   KC.A,     KC.B,    KC.C,
        KC.D,   KC.E,     KC.F,    KC.G,
        KC.H,   KC.I,     KC.J,    KC.K,
    ],
    [
        LA0,  KC.N1,  KC.N2,  KC.N3,
        KC.N4,  KC.N5,  KC.N6,  KC.N7,
        KC.N8,  KC.N9 
    ]
]

# KEYMAP for encoders
encoders.map = [    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.MUTE)), 
]

# KEYMAP for analog keys 
ana.map = [
    [
        KC.W,KC.A,KC.S,KC.D
    ],
    [
        KC.N1,KC.N2,KC.N3,KC.N4
    ]
]

if __name__ == '__main__':
    keyboard.go() 
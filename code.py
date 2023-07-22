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

from kmk.modules.analouge import AnalogKey #handles analoginput


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



___ = KC.TRNS
xxx = KC.NO
LA1 = KC.MO(1)

# KEYMAPS 
keyboard.keymap = [
    # MACRO
    [
        KC.M,   LA1,     KC.C,    KC.D,
        KC.E,   KC.F,     KC.G,    KC.H,
        KC.I,   KC.J,     KC.K,    KC.L,
    ],
    [
        KC.N1,  KC.N2,  KC.N3,  KC.N4,
        KC.N5,  KC.N6,  KC.N7,  KC.N8,
        KC.N9,
    ]
]

encoders.map = [    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.MUTE)),   # MACROS
]
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
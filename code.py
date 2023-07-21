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

#tapdance = TapDance()
#tapdance.tap_time = 250
keyboard.modules = [layers, encoders] #tapdance]

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

# ANALOG INPUT
analog_key_module = AnalogKey(board.GP29,board.GP28,board.GP27,board.GP26, 50000) #pass 4 analog pins and threshold 
keyboard.modules.append(analog_key_module)

_______ = KC.TRNS
xxxxxxx = KC.NO

# KEYMAPS
keyboard.keymap = [
    # MACROS
    [
        KC.VOLD,   KC.B,     KC.C,    KC.D,
        KC.E,   KC.F,     KC.G,    KC.H,
        KC.I,   KC.J,     KC.K,    KC.L,
    ]
]

encoders.map = [    ((KC.VOLD, KC.VOLU, KC.MUTE),           (KC.RGB_VAD,    KC.RGB_VAI,     KC.MUTE)),   # MACROS
]

if __name__ == '__main__':
    keyboard.go()
import analogio
import board

from kmk.modules import Module
from kmk.keys import KC

class AnalogKey(Module):
    def __init__(self):
        self.map = None
        self.pin1 = analogio.AnalogIn(board.GP29)
        self.pin2 = analogio.AnalogIn(board.GP28)
        self.pin3 = analogio.AnalogIn(board.GP27)
        self.pin4 = analogio.AnalogIn(board.GP26)
        self.threshold = 50000

    def before_matrix_scan(self, keyboard):
        layer_id = keyboard.active_layers[0]
        #print(layer_id)
        #print(f's',self.map[layer_id][0])
        if self.pin1.value > self.threshold:
            keyboard.add_key(self.map[layer_id][0])
        else:
            keyboard.remove_key(self.map[layer_id][0])
            
        """if self.pin2.value > self.threshold:
            keyboard.add_key(KC.A)
        else:
            keyboard.remove_key(KC.A)
            
        if self.pin3.value > self.threshold:
            keyboard.add_key(KC.S)
        else:
            keyboard.remove_key(KC.S)
            
        if self.pin4.value > self.threshold:
            keyboard.add_key(KC.D)
        else:
            keyboard.remove_key(KC.D)"""
        

            
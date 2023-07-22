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
        #print(self.pin1.value,self.pin2.value,self.pin3.value,self.pin4.value)
        
        if self.pin1.value > self.threshold:
            keyboard.add_key(self.map[layer_id][0])
        else:
            keyboard.remove_key(self.map[layer_id][0])
        
        if self.pin2.value > self.threshold:
            keyboard.add_key(self.map[layer_id][1])
        else:
            keyboard.remove_key(self.map[layer_id][1])
        
        if self.pin3.value > self.threshold:
            keyboard.add_key(self.map[layer_id][2])
        else:
            keyboard.remove_key(self.map[layer_id][2])
        
        if self.pin4.value > self.threshold:
            keyboard.add_key(self.map[layer_id][3])
        else:
            keyboard.remove_key(self.map[layer_id][3])
            
        
        

            
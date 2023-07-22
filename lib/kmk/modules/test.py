import analogio
import board

from kmk.modules import Module
from kmk.keys import KC

class testA(Module):
    def __init__(self):
        #self.pin1 = analogio.AnalogIn(board.GP29)
        i=1
        
    def before_matrix_scan(self, keyboard):
        #print(self.pin1.value)
        i=2
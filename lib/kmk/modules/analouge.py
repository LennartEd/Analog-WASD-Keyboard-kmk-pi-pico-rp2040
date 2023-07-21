import analogio

from kmk.modules import Module
from kmk.keys import KC

#

class AnalogKey(Module):
    def __init__(self, pin1,pin2,pin3,pin4, threshold):
        self.pin1 = analogio.AnalogIn(pin1)
        self.pin2 = analogio.AnalogIn(pin2)
        self.pin3 = analogio.AnalogIn(pin3)
        self.pin4 = analogio.AnalogIn(pin4)
        self.threshold = threshold

    def before_matrix_scan(self, keyboard):
        #print(self.pin.value)
        if self.pin1.value > self.threshold:
            keyboard.add_key(KC.W)
        else:
            keyboard.remove_key(KC.W)
            
        if self.pin2.value > self.threshold:
            keyboard.add_key(KC.A)
        else:
            keyboard.remove_key(KC.A)
            
        if self.pin3.value > self.threshold:
            keyboard.add_key(KC.S)
        else:
            keyboard.remove_key(KC.S)
            
        if self.pin4s.value > self.threshold:
            keyboard.add_key(KC.D)
        else:
            keyboard.remove_key(KC.D)
        

            
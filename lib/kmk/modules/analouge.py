import analogio
import board

from kmk.modules import Module
from kmk.keys import KC

class AnalogKey(Module):
    def __init__(self):
        self.map = None
        self.pins = None
        self.threshold = 50000
        self.state = [1,0,1,0,1,0,1,0]
        
    def during_bootup(self, keyboard):
        self.pin1 = analogio.AnalogIn(self.pins[0])
        self.pin2 = analogio.AnalogIn(self.pins[1])
        self.pin3 = analogio.AnalogIn(self.pins[2])
        self.pin4 = analogio.AnalogIn(self.pins[3])
        return

    def before_matrix_scan(self, keyboard):
        layer_id = keyboard.active_layers[0]
        print(self.pin1.value)#,self.pin2.value,self.pin3.value,self.pin4.value) 
        #print(self.state)
        
        if self.pin1.value > self.threshold and self.state[0]==1:
            keyboard.add_key(self.map[layer_id][0])
            self.state[0]=0
            self.state[1]=1
        if self.pin1.value < self.threshold and self.state[1]==1:
            keyboard.remove_key(self.map[layer_id][0])
            self.state[1]=0
            self.state[0]=1
        
        if self.pin2.value > self.threshold and self.state[2]==1:
            keyboard.add_key(self.map[layer_id][1])
            self.state[2]=0
            self.state[3]=1
        if self.pin2.value < self.threshold and self.state[3]==1:
            keyboard.remove_key(self.map[layer_id][1])
            self.state[3]=0
            self.state[2]=1
        
        if self.pin3.value > self.threshold and self.state[4]==1:
            keyboard.add_key(self.map[layer_id][2])
            self.state[4]=0
            self.state[5]=1
        if self.pin3.value < self.threshold and self.state[5]==1:
            keyboard.remove_key(self.map[layer_id][2])
            self.state[5]=0
            self.state[4]=1
        
        if self.pin4.value > self.threshold and self.state[6]==1:
            keyboard.add_key(self.map[layer_id][3])
            self.state[6]=0
            self.state[7]=1
        if self.pin4.value < self.threshold and self.state[7]==1:
            keyboard.remove_key(self.map[layer_id][3])
            self.state[7]=0
            self.state[6]=1
            
        
        

            
import analogio
import board
import time

from kmk.modules import Module
from kmk.keys import KC

class AnalogKey(Module):
    def __init__(self):
        self.reverse = None
        self.c = 0
        self.st = 0
        self.end = 0
        self.map = None
        self.pins = None
        self.threshold = None
        self.keypType = None
        self.lastVal = [0,0,0,0]
        self.state = [1,0,1,0,1,0,1,0]
        
    def during_bootup(self, keyboard):
        self.pin1 = analogio.AnalogIn(self.pins[0])
        self.pin2 = analogio.AnalogIn(self.pins[1])
        self.pin3 = analogio.AnalogIn(self.pins[2])
        self.pin4 = analogio.AnalogIn(self.pins[3])
        return

    def before_matrix_scan(self, keyboard):
        layer_id = keyboard.active_layers[0]
        #print(layer_id)
        #print(self.pin1.value,self.pin2.value,self.pin3.value,self.pin4.value)
        #time.sleep(0.1)
        
        #threshold mode
        if self.keypType[layer_id] == 0: #Threshold
            #when analog value is smaller than threshold and threshold wasnt surpassed before reseting and the direction is not reversed
                #then key is pressed(from the map [in layer][at position])
                #then state is switched so the keypress is only sent once (could probably be removed but may help with speed)
                
            #key1
            if (self.pin1.value < self.threshold[0] and self.state[0] == 1 and not self.reverse) or (self.pin1.value > self.threshold[0] and self.state[0] == 1 and self.reverse):
                keyboard.add_key(self.map[layer_id][0])
                self.state[0]=0
                self.state[1]=1
            elif (self.pin1.value > self.threshold[0] and self.state[1] == 1 and not self.reverse) or (self.pin1.value < self.threshold[0] and self.state[1] == 1 and self.reverse):
                keyboard.remove_key(self.map[layer_id][0])
                self.state[1]=0
                self.state[0]=1
            
            #key2
            if (self.pin2.value < self.threshold[0] and self.state[2] == 1 and not self.reverse) or (self.pin2.value > self.threshold[0] and self.state[2] == 1 and self.reverse):
                keyboard.add_key(self.map[layer_id][1])
                self.state[2]=0
                self.state[3]=1
            elif (self.pin2.value > self.threshold[0] and self.state[3] == 1 and not self.reverse) or (self.pin2.value < self.threshold[0] and self.state[3] == 1 and self.reverse):
                keyboard.remove_key(self.map[layer_id][1])
                self.state[3]=0
                self.state[2]=1
            
            #key3
            if (self.pin3.value < self.threshold[0] and self.state[4] == 1 and not self.reverse) or (self.pin3.value > self.threshold[0] and self.state[4] == 1 and self.reverse):
                keyboard.add_key(self.map[layer_id][2])
                self.state[4]=0
                self.state[5]=1
            elif (self.pin3.value > self.threshold[0] and self.state[5] == 1 and not self.reverse) or (self.pin3.value < self.threshold[0] and self.state[5] == 1 and self.reverse):
                keyboard.remove_key(self.map[layer_id][2])
                self.state[5]=0
                self.state[4]=1
            
            #key4
            if (self.pin4.value < self.threshold[0] and self.state[6] == 1 and not self.reverse) or (self.pin4.value > self.threshold[0] and self.state[6] == 1 and self.reverse):
                keyboard.add_key(self.map[layer_id][3])
                self.state[6]=0
                self.state[7]=1
            elif (self.pin4.value > self.threshold[0] and self.state[7] == 1 and not self.reverse) or (self.pin4.value < self.threshold[0] and self.state[7] == 1 and self.reverse):
                keyboard.remove_key(self.map[layer_id][3])
                self.state[7]=0
                self.state[6]=1
       #-------------------------------------------------------------------------------------------------------------------------------------------------  
        #rapid trigger mode
        if self.keypType[layer_id] == 1:
            #key1
            if (self.pin1.value > self.lastVal[0]+self.threshold[1] and not self.reverse) or (self.pin1.value < self.lastVal[0]-self.threshold[1] and self.reverse):
                keyboard.remove_key(self.map[layer_id][0])
                self.lastVal[0] = self.pin1.value  
                self.state[0]=0
                self.state[1]=1
            elif (self.pin1.value < self.lastVal[0]-self.threshold[1] and not self.reverse) or (self.pin1.value > self.lastVal[0]+self.threshold[1] and self.reverse):
                keyboard.add_key(self.map[layer_id][0])
                self.lastVal[0] = self.pin1.value  
                self.state[1]=0
                self.state[0]=1
                
            #key2
            if (self.pin2.value > self.lastVal[1]+self.threshold[1] and not self.reverse) or (self.pin2.value < self.lastVal[1]-self.threshold[1] and self.reverse):
                keyboard.remove_key(self.map[layer_id][1])
                self.lastVal[1] = self.pin2.value
                self.state[2]=0
                self.state[3]=1
            elif (self.pin2.value < self.lastVal[1]-self.threshold[1] and not self.reverse) or (self.pin2.value > self.lastVal[1]+self.threshold[1] and self.reverse):
                keyboard.add_key(self.map[layer_id][1])
                self.lastVal[1] = self.pin2.value
                self.state[3]=0
                self.state[2]=1
            
            #key3
            if (self.pin3.value > self.lastVal[2]+self.threshold[1] and not self.reverse) or (self.pin3.value < self.lastVal[2]-self.threshold[1] and self.reverse):
                keyboard.remove_key(self.map[layer_id][2])
                self.lastVal[2] = self.pin3.value
                self.state[4]=0
                self.state[5]=1
            elif (self.pin3.value < self.lastVal[2]-self.threshold[1] and not self.reverse) or (self.pin3.value > self.lastVal[2]+self.threshold[1] and self.reverse):
                keyboard.add_key(self.map[layer_id][2])
                self.lastVal[2] = self.pin3.value
                self.state[5]=0
                self.state[4]=1
            
            #key4
            if (self.pin4.value > self.lastVal[3]+self.threshold[1] and not self.reverse) or (self.pin4.value < self.lastVal[3]-self.threshold[1] and self.reverse):
                keyboard.remove_key(self.map[layer_id][3])
                self.lastVal[3] = self.pin4.value
                self.state[6]=0
                self.state[7]=1
            elif (self.pin4.value < self.lastVal[3]-self.threshold[1] and not self.reverse) or (self.pin4.value > self.lastVal[3]+self.threshold[1] and self.reverse):
                keyboard.add_key(self.map[layer_id][3])
                self.lastVal[3] = self.pin4.value
                self.state[7]=0
                self.state[6]=1
             
        
        

            
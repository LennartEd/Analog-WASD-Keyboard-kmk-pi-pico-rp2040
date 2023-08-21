import time
import board
import analogio
import math

a1 = analogio.AnalogIn(board.GP29)
a2 = analogio.AnalogIn(board.GP28)
a3 = analogio.AnalogIn(board.GP27)
a4 = analogio.AnalogIn(board.GP26)
last = a1.value
maxDiv = 0

for _ in range(10):
    for _ in range(10000):
        val = []
        
        for _ in range(2):
            val.append(a1.value)
            
        div = abs(max(val)-min(val))
        if div>maxDiv:maxDiv=div
    print(maxDiv)
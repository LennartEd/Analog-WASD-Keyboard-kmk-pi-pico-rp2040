#Analog-WASD-Keyboard-kmk-pi-pico-rp2040

A Raspberry pi pico(rp2040) kmk keyboard with analog WASD input. 
---
OVERVIEW
This is a kmk keyboard using an RP2040 with analog WASD keys.
The WASD keys use linear Hall effect sensors 
---
COMPONENTS
4 

CODE
Added module: analouge.py 


pin assignment: code.py -> ana.pins =()
keymap for analog keys can be defined it code.py -> ana.map = []

GOALS:
-analog input using magnetic switches(wooting lekker) and hall effect sensors as WASD
-normal and rapid trigger mode

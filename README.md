#Analog-WASD-Keyboard-kmk-pi-pico-rp2040

A Raspberry pi pico(rp2040) kmk keyboard with analog WASD input. 
---

OVERVIEW
---
This is a kmk keyboard using an RP2040 with analog WASD keys.

As kmk is circuitpython based this should work on any [circuitpython compatible boards](https://circuitpython.org/downloads) with 4 analog inputs.
The WASD keys use linear Hall effect sensors and magnetic keys. 
The rest of the keys use normal mechanical keys.
This is just the base code for the analog keys. I added a normal 4x3 key matrix as an example but you can add how many your desired layout needs.

As i will be building a fully analog keyboard i only build a WASD prototype. 
Everything should be working though. If you have questions or find errors please let me know.


COMPONENTS
---
+ 1 RP2040 or Circuitpython compatible board (IMPORTANT: you need one with 4 analog inputs which the original pipico does not have. I used [PR2040-Zero](https://circuitpython.org/board/waveshare_rp2040_zero/) and [yd-rp2040](https://circuitpython.org/board/vcc_gnd_yd_rp2040/)


+ 4 Linear Hall effect sensors (any should work but i used [HUAXIN HX6659IUA-B](https://www.lcsc.com/product-detail/_HUAXIN-_C495741.html)or [GH39FKSW](https://www.lcsc.com/product-detail/_GoChip-Elec-Tech-Shanghai-_C266230.html))


+ 4 magnetic key switches (I used [wooting lekker](https://wooting.io/product/lekker-switch-linear60])


+ (capacitors 100nF-10000nF ) not strictly nececary but reduces noise. 10000nF gave me the best results.


+ Normal mechanical keys


+ Diodes


+ (rotary encoders)

BUILDING NOTES
---
As i have only build a prototype and not a full keyboard you'll have to make your own case or use someone elses from the internet.


CODE
---
When [circuitpython is installed](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) move the content of the code folder into the RP2040.

Added module: analog.py which handles the analog key presses.

Basic variables for the analog keys can be changed in the main code.py file so this file does not have to be touched.

If you're getting ghost presses when using rapid Trigger use the "maxChangeInVal.py"+ 300 to find a siutable value for your keyboard.

Pin assignment for analog keys can be done in: code.py -> ana.pins =()

The key map for analog keys can be defined it code.py -> ana.map = []

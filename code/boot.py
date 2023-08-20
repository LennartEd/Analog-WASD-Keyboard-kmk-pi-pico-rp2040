"""import supervisor
import board
import storage
import usb_cdc
import digitalio

button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

if button.value:
    storage.disable_usb_drive() # Hides device storage
    usb_cdc.disable() # Disables serial comunication
    usb_midi.disable() # Disables midi
    usb_hid.enable(boot_device=1) # Enables keyboard before OS boot
    
button.deinit()"""

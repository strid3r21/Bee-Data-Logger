import time, gc, os
import neopixel
import board, digitalio
import bdl

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB)

while True:
    
	# common color RGB values.
	#green = 0,150,0
	#red = 150,0,0
	#blue = 0,0,150
	#pink = 255,20,147
	#purple = 148,0,211
	#yellow = 242,239,61
	#white = 255,255,255
	#aqua = 0,255,255
	#orange = 255,165,0
	#off = 0,0,0

	#set the RGB LED to Green
    pixel[0] = ( 0, 150, 0, 0.5)
    time.sleep(1)
    #set the RGB LED to Red
    pixel[0] = ( 150, 0, 0, 0.5)
    time.sleep(1)
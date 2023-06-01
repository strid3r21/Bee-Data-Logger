import time, gc, os
import neopixel
import board, digitalio
import bdl

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB)

# Create a colour wheel index int
color_index = 0

# Rainbow colours on the NeoPixel
while True:
    # Get the R,G,B values of the next colour
    r,g,b = bdl.rgb_color_wheel( color_index )
    # Set the colour on the NeoPixel
    pixel[0] = ( r, g, b, 0.5)
    # Increase the wheel index
    color_index += 1

    # Sleep for 15ms so the colour cycle isn't too fast
    time.sleep(0.015)
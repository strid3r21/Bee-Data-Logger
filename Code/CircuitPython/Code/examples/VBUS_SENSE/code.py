import time, gc, os
import neopixel
import board, digitalio
import bdl

# Create a NeoPixel instance
# Brightness of 0.3 is ample for the 1515 sized LED
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3, auto_write=True, pixel_order=neopixel.GRB)


# this code will detect if the USB is plugged in. this can be useful if you want your code to stop running when you've 
# plugged your board into your board or vise versa
while True:
        vbus =  bdl.get_vbus_present()
        if vbus == False:
                pixel[0] = ( 255, 0, 0, 0.5)
                pixel.write()
        if vbus == True :
                pixel[0] = ( 0, 255, 0, 0.5)
                pixel.write()
        time.sleep(.5) 
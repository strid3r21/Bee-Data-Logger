
import adafruit_sdcard
import board
import digitalio
import storage
import time


spi = board.SPI()
cs = digitalio.DigitalInOut(board.SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
time.sleep(1)
storage.mount(vfs, "/sd")

with open("/sd/test.txt", "w") as f:
    f.write("Hello world!\r\n")

with open("/sd/test.txt", "r") as f:
    print("Read line from file:")
    print(f.readline(), end='')

with open("/sd/test.txt", "a") as f:
    f.write("This is another line!\r\n")

with open("/sd/test.txt", "r") as f:
    print("Printing lines in file:")
    line = f.readline()
    while line != '':
        print(line, end='')
        line = f.readline()




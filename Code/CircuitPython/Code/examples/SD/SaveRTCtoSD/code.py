import bdl
import adafruit_sdcard
import storage
import digitalio
import board
import time


spi = board.SPI()
cs = digitalio.DigitalInOut(board.SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
time.sleep(1)
storage.mount(vfs, "/sd")


while True:
    # open file for append
    with open("/sd/dateTime.txt", "a") as f:
        RTC = bdl.rtc.datetime
        temp = (bdl.rtc.temperature * 1.8) + 32
        f.write(str("Date: {} {}/{}/{}".format(
                bdl.days[int(RTC.tm_wday)], RTC.tm_mon, RTC.tm_mday, RTC.tm_year
            )) + " " + str("Time: {}:{:02}:{:02}".format(RTC.tm_hour, RTC.tm_min, RTC.tm_sec) +" "+ "Temp: f°%0.1f\n" % temp))
        
    # file is saved
    time.sleep(60)

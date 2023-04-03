import bdl
import alarm
import board
import digitalio
import time
import adafruit_sdcard
import storage

spi = board.SPI()
cs = digitalio.DigitalInOut(board.SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
time.sleep(1)
storage.mount(vfs, "/sd")

# Create a an alarm that will trigger 20 seconds from now.
# Exit the program, and then deep sleep until the alarm wakes us.

  # open file for append
with open("/sd/dateTime.txt", "a") as f:
        RTC = bdl.rtc.datetime
        temp = (bdl.rtc.temperature * 1.8) + 32
        f.write(str("Date: {} {}/{}/{}".format(
                bdl.days[int(RTC.tm_wday)], RTC.tm_mon, RTC.tm_mday, RTC.tm_year
            )) + " " + str("Time: {}:{:02}:{:02}".format(RTC.tm_hour, RTC.tm_min, RTC.tm_sec) +" "+ "Temp: f°%0.1f\n" % temp))
        
time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 20)
alarm.exit_and_deep_sleep_until_alarms(time_alarm)
# Does not return, so we never get here.
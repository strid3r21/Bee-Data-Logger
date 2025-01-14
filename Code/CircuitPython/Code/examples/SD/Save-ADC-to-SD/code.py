import bdl
import adafruit_sdcard
import storage
import digitalio
import board
import time

from analogio import AnalogIn

pin3 = AnalogIn(board.A3) #setup your ADC pins 
pin4 = AnalogIn(board.A4) # the bee data logger has ADC on pins 3 through 9
pin5 = AnalogIn(board.A5) 
pin6 = AnalogIn(board.A6) 
pin7 = AnalogIn(board.A7) 
pin8 = AnalogIn(board.A8) 
pin9 = AnalogIn(board.A9) 

file_path = "/sd/data.txt"
header = "Date, Time, Temp, ADC3 Voltage\n"

spi = board.SPI()
cs = digitalio.DigitalInOut(board.SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
time.sleep(1)
storage.mount(vfs, "/sd")

if False:  # change to True if you want to set the time!
    #                     year, mon, date, hour, min, sec, wday, yday, isdst
    t = time.struct_time((2023, 6,   1,   12,   35, 2,   0,    -1,   -1))
    # you must set year, mon, date, hour, min, sec and weekday
    # yearday is not supported, isdst can be set but we don't do anything with it at this time
    print("Setting time to:", t)  # uncomment for debugging
    bdl.rtc.datetime = t
    print()

while True:
    #pin 3 is shown, but you can do this for all the ADC pins, just set them up like this.
    adc_3 = bdl.get_adc_voltage(pin3)
    print("ADC3 Voltage: %0.3fv" % adc_3) # prints the ADC voltage reading, the %0.3f formats the voltage to just 3 decimal places past zero. 0.000v instead of 0.0000000v
    print("ADC3_Raw", pin3.value) # prints the raw ADC reading
    
    adc_4 = bdl.get_adc_voltage(pin4)
    print("ADC4 Voltage: %0.3fv" % adc_4) 
    print("ADC4_Raw", pin4.value)
    
	# adc_5
	# adc_6
	# etc etc etc
    

    with open("/sd/adc_readings.txt", "a") as f:
        RTC = bdl.rtc.datetime
        temp = (bdl.rtc.temperature * 1.8) + 32
        f.write(str("Date: {} {}/{}/{}".format(bdl.days[int(RTC.tm_wday)], RTC.tm_mon, RTC.tm_mday, RTC.tm_year) + ", " +\
        "Time: {}:{:02}:{:02}".format(RTC.tm_hour, RTC.tm_min, RTC.tm_sec) +" ,"+ "Temp: f°%0.1f" % temp + " ," +\
        "ADC3 Voltage: %0.3f" % adc_3 + " ," + "ADC4 Voltage: %0.3f" % adc_4 +"\n"))
        time.sleep(5)

# Updating just the UF2 firmware. 

Hit reset and then boot in guick succession which will give access to the Bee S3's bootloader drive which is call BEES3BOOT.
with this drive open just drag the firmware.uf2 file to the drive and it will update the UF2 firmware.

You can find the most up to date UF2 firmware here - https://circuitpython.org/board/smartbeedesigns_bee_data_logger/

# Flashing Circuit Python Firmware onto your Bee Data Logger.

put the board into download mode by holding boot button and pressing reset button then release both buttons. <br/>

Use esptool to erease flash and then flash new firmware onto the board.

# Erase the flash.
### Linux
```bash
esptool.py --chip esp32s3 --port /dev/ttyACM0 erase_flash
```

### Mac
Please do a `ls /dev/cu.usbm*` to determine the port your board has enumerated as.
```bash
esptool.py --chip esp32s3 --port /dev/cu.usbmodem01 erase_flash
```

### Windows
Change xxx to whatever COM port is being used by the board
```bash
esptool.py --chip esp32s3 --port COMxxx erase_flash
```
# Flash new Firmware

### Linux
````
esptool.py --chip esp32s3 --port /dev/ttyACM0 --before=default_reset --after=no_reset write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x0 bootloader.bin 0x8000 partition-table.bin 0xe000 ota_data_initial.bin 0x410000 tinyuf2.bin
````

### Mac
Please do a `ls /dev/cu.usbm*` to determine the port your board has enumerated as.
````
esptool.py --chip esp32s3 --port /dev/cu.usbmodem01 --before=default_reset --after=no_reset write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x0 bootloader.bin 0x8000 partition-table.bin 0xe000 ota_data_initial.bin 0x410000 tinyuf2.bin
````

### Windows
````
esptool.py --chip esp32s3 -p COMxxx --before=default_reset --after=no_reset write_flash --flash_mode dio --flash_size detect --flash_freq 80m 0x0 bootloader.bin 0x8000 partition-table.bin 0xe000 ota_data_initial.bin 0x410000 tinyuf2.bin
````

Once that is done you should see a new drive show up called BDLBOOT.<br/>

Open that up and drag the firmware.uf2 file onto it.<br/>

The BDLBOOT drive will disappear and come back after a few seconds as CIRCUITPY.<br/>

You're now good to use circuit python on the board!

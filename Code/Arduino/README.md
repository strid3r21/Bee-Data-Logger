# Programming on Arduino

## Add the Espressif ESP32 arduino board library to Arduino IDE
File > Preferences > at the bottom "Additional Board Manager URLS" paste in this url
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json 
 
From there you will be able to search and add the ESP32 board library from the board library search bar. install the ESP32 library by Espressif and make sure you're using version number 2.0.5 or later. You will then be able to select your Bee Data Logger from the board manager.

## How to program the Bee Data Loggger
In order to program the Bee Data Logger you need to put it into download mode. To do so all you need to do is connect the USB-C cable and then press and hold the boot button. with the boot button being held down, press the reset button and release. then you can release the boot button. this will put the Bee Data Logger into download mode which will allow it to be programmed. Then for the board, select "Bee Data Logger" from the board manager.

# Bee Data Logger Arduino Example Sketches & helper library

Examples can be found in the [Bee Data Logger Arduino Helper](https://github.com/strid3r21/BeeDataLogger-Arduino-Helper) repo OR these can also be loaded from the examples menu in the Arduino IDE.

## Installation

This library can be installed through the Arduino library manager or manually from github by following [the instructions here](https://docs.arduino.cc/software/ide-v1/tutorials/installing-libraries).

## List of functions

```c++

void begin();

// Set LDO2 on or off
void setLDO2Power(bool on);

// Set neopixel power on or off
void setPixelPower(bool on);

// Set neopixel color
void setPixelColor(uint8_t r, uint8_t g, uint8_t b);
void setPixelColor(uint32_t rgb);
void setPixelColor(green);  //green, red, blue, yellow, pink, purple, orange, white, aqua, off

// Set neopixel brightness
void setPixelBrightness(uint8_t brightness);

// Pack r,g,b (0-255) into a 32bit rgb color
static uint32_t color(uint8_t r, uint8_t g, uint8_t b);

// Convert a color wheel angle (0-255) to a 32bit rgb color
static uint32_t colorWheel(uint8_t pos);

// Get the battery voltage in volts
float getBatteryVoltage();

// Detect if VBUS (USB power) is present
bool getVbusPresent();

```

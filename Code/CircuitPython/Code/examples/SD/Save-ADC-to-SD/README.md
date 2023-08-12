## Save the ADC readings to the sd card

This code shows how to save the ADC voltage and ADC raw readings from the ADC pins on the bee data logger.

Pins 3 through 9 on the bee data logger have ADC capabilities.

when the pins are left floating you may see the readings "float" around. but once they're pulled HIGH (with a voltage between 0 & 3.3v) or LOW (to ground) the readings should stabilize.


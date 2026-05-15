from gpiozero import RGBLED
from signal import pause

led = RGBLED(red=9, green=10, blue=11)

led.red = 1.0
led.green = 1.0
led.blue = 1.0

pause()

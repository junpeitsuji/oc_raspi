from gpiozero import RGBLED

led = RGBLED(red=9, green=10, blue=11)

led.red = 0.0
led.green = 0.0
led.blue = 1.0

input()

from gpiozero import RGBLED
from gpiozero import Button
from time import sleep

led = RGBLED(red=9, green=10, blue=11)

button = Button(2)

colors = [(1,0,0), (1,1,0), (0,1,0), (0,1,1), (0,0,1), (1,0,1)]

i = 0
while True:
    if button.is_pressed:
        led.color = colors[i % 6]
        sleep(0.05)
        i += 1
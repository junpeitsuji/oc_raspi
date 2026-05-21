from gpiozero import RGBLED

# フルカラーLEDをGPIO 9〜11に接続
led = RGBLED(red=9, green=10, blue=11)

led.red = 1.0
led.green = 0.0
led.blue = 0.0

input()   # キーボード入力待ち

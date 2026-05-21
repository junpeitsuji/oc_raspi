from gpiozero import RGBLED, Button
from time import sleep

# タクトスイッチをGPIO 2に接続
button = Button(2)

# フルカラーLEDをGPIO 9〜11に接続
led = RGBLED(red=9, green=10, blue=11)

# 順に表示するカラーを配列に設定（赤、黄、緑、シアン、青、紫）
colors = [(1,0,0), (1,1,0), (0,1,0), (0,1,1), (0,0,1), (1,0,1)]

i = 0
while True:
    if button.is_pressed:
        # スイッチが押されたときだけ色を変更
        led.color = colors[i % 6]
        sleep(0.05)
        i += 1

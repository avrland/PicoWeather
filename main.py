from machine import I2C, Pin, Timer
from sensors import *
from ssd1306 import *
import utime as time

debug = 0
tempNum = 1

oled = SSD1306Init(0, 17, 16)
newSensors = Sensors(1, 2, 3, 28)
newSensors.BmpInit()
newSensors.DhtInit()

def tick(timer):
    global newSensors, oled, ShowData, tempNum
    wynik = newSensors.GetValues()
    ShowData(oled, wynik, tempNum)
    if(tempNum==1):
         tempNum=2
    else:
         tempNum=1

tim = Timer()
tim.init(freq=0.5, mode=Timer.PERIODIC, callback=tick)
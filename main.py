from machine import I2C, Pin, Timer
from sensors import *
from ssd1306 import *
import utime as time

debug = 0
tempNum = 1


newSensors = Sensors(0, 16, 17, 15)
i2cbus = newSensors.BmpInit()
newSensors.DhtInit()
oled = SSD1306Init(i2cbus)

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
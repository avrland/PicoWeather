from machine import *
from sensors import *
from ssd1306 import *

newSensors = 0
oled = 0
tempNum = 1

def AppInit():
     global newSensors, oled, rtc
     newSensors = Sensors(0, 16, 17, 15)
     i2cbus = newSensors.BmpInit()
     newSensors.DhtInit()
     oled = SSD1306Init(i2cbus)
     rtc = RTC()
     rtc.datetime((2022, 3, 3, 1, 8, 0, 0, 0))

def AppLoop(timer):
    global newSensors, oled, ShowData, tempNum
    wynik = newSensors.GetValues()
    ShowData(oled, wynik, tempNum, rtc.datetime())
    tempNum += 1
    if(tempNum>4): tempNum=1

     
AppInit()
tim = Timer()
tim.init(freq=0.5, mode=Timer.PERIODIC, callback=AppLoop)
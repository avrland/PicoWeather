from machine import *
from sensors import *
from ssd1306 import *
import utime as time
import _thread
newSensors = 0
oled = 0
tempNum = 1
appTick = 1
doTask = 0
wynik = 0

def AppInit():
     global newSensors, oled, rtc, wynik, AppLoop
     newSensors = Sensors(0, 16, 17, 15)
     newSensors.DhtInit()
     time.sleep(1)
     i2cbus = newSensors.BmpInit()
     oled = SSD1306Init(i2cbus)
     rtc = RTC()
     rtc.datetime((2022, 3, 3, 1, 8, 0, 0, 0))
     wynik = newSensors.GetValues()
     tim = Timer()
     tim.init(freq=1, mode=Timer.PERIODIC, callback=AppTick)

def AppTick(timer):
     global appTick, doTask
     appTick += 1
     doTask = 1
     if(appTick>20): appTick = 1
     
AppInit()

while 1:
     if(doTask==1):
          if(appTick%2==1):
               print("Pomiar")
               wynik = newSensors.GetValues()
          if(appTick%2==0):
               print("Wyswietlanie wynikow")
               ShowData(oled, wynik, tempNum, rtc.datetime())
               tempNum += 1
               if(tempNum>4): tempNum=1     
          doTask = 0
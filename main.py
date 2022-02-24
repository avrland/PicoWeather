from machine import I2C, Pin
from sensors import *
from ssd1306 import *
import utime as time

debug = 0

oled = SSD1306Init(0, 17, 16)
newSensors = Sensors(1, 2, 3, 28)
newSensors.BmpInit()
newSensors.DhtInit()

while 1:
    wynik = newSensors.GetValues()
    ShowData(oled, wynik)
    time.sleep(2)
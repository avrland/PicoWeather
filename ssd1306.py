from machine import I2C, Pin
import utime as time
from ssd1306_driver import SSD1306_I2C
debug = 0

def SSD1306Init(i2c_id, scl, sda):
    WIDTH  = 128                                            # oled display width
    HEIGHT = 32                                             # oled display height
    i2c = I2C(i2c_id, scl=Pin(scl), sda=Pin(sda), freq=20000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
    if(debug):
        devices = i2c.scan()
        print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
        print("I2C Configuration: "+str(i2c))                   # Display I2C config
    oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
    return oled
def ShowData(oled, values):
    oled.fill(0)
    oled.text("T1:{}".format(values[0]) + "C",0,0)
    oled.text("Rh: {}".format(values[1]) + " %",0,10)
    oled.text("p: " + str(values[3]) + " hPa",0,20)
    oled.text("T2:{}".format(values[2]) + "C", 70, 0)
    oled.show()
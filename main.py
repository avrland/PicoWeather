from machine import I2C, Pin
from sensors import *
import utime as time
from ssd1306 import SSD1306_I2C

def ssd1306Init():
    WIDTH  = 128                                            # oled display width
    HEIGHT = 32                                             # oled display height
    i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=20000)       # Init I2C using pins GP8 & GP9 (default I2C0 pins)
    devices = i2c.scan()
    #print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
    #print("I2C Configuration: "+str(i2c))                   # Display I2C config
    oled = SSD1306_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display
    return oled

dht_sensor = DhtInit(28) #1wire pin
time.sleep(1)
bmp_sensor = BmpInit(1, 2, 3) #I2c, SDA pin, SCL pin
time.sleep(1)
oled = ssd1306Init() #I2c, SDA pin, SCL pin
time.sleep(1)

while 1:
    #print("BMP280 Temp: " + str(bmp_sensor.temperature) + " °C")
    #print("BMP280 Pressure: " + str(bmp_sensor.pressure/100) + " hPa")
    
    oled.fill(0)
    oled.text("T1:{}".format(dht_sensor.temperature) + "C",0,0)
    oled.text("Rh: {}".format(dht_sensor.humidity) + " %",0,10)
    oled.text("p: " + str(bmp_sensor.pressure/100) + " hPa",0,20)
    oled.text("T2:{}".format(bmp_sensor.temperature) + "C", 70, 0)
    oled.show()
    time.sleep(1)

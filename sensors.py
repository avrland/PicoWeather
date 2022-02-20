from machine import I2C, Pin
from bmp280 import *
import utime as time
from dht import DHT11, InvalidChecksum

bmpSdaPin = 0
bmpSclPin = 1
bmpI2c = 0
dht11Pin = 28

def BmpInit():
    bus = I2C(bmpI2c, sda=Pin(bmpSdaPin), scl=Pin(bmpSclPin)) 
    bmp = BMP280(bus)
    bmp.use_case(BMP280_CASE_WEATHER)
    bmp.oversample(BMP280_OS_HIGH)
    bmp.temp_os = BMP280_TEMP_OS_8
    bmp.press_os = BMP280_PRES_OS_4
    bmp.standby = BMP280_STANDBY_250
    bmp.iir = BMP280_IIR_FILTER_2
    bmp.spi3w = BMP280_SPI3W_ON
    bmp.power_mode = BMP280_POWER_NORMAL
    return bmp
def DhtInit():
    pin = Pin(dht11_pin, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    return sensor
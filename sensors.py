from machine import I2C, Pin
from bmp280 import *
import utime as time
from dht import DHT11, InvalidChecksum

class Sensors:
    def __init__(self, bmpI2c, bmpSdaPin, bmpSclPin, dht11Pin):
        self.bmpI2c = bmpI2c
        self.bmpSdaPin = bmpSdaPin
        self.bmpSclPin = bmpSclPin
        self.dht11Pin = dht11Pin
    def BmpInit(self):
        bus = I2C(self.bmpI2c, sda=Pin(self.bmpSdaPin), scl=Pin(self.bmpSclPin), freq=100000) 
        bmp = BMP280(bus)
        bmp.use_case(BMP280_CASE_WEATHER)
        bmp.oversample(BMP280_OS_HIGH)
        bmp.temp_os = BMP280_TEMP_OS_8
        bmp.press_os = BMP280_PRES_OS_4
        bmp.standby = BMP280_STANDBY_250
        bmp.iir = BMP280_IIR_FILTER_2
        bmp.spi3w = BMP280_SPI3W_ON
        bmp.power_mode = BMP280_POWER_NORMAL
        self.bmp = bmp
        return bus
    def DhtInit(self):
        pin = Pin(self.dht11Pin, Pin.OUT, Pin.PULL_DOWN)
        self.dht = DHT11(pin)
        return self.dht
    def GetValues(self):
        values = []
        values.append(self.bmp.temperature)
        values.append(self.bmp.pressure/100)
        values.append(self.dht.temperature)
        values.append(self.dht.humidity)
        return values
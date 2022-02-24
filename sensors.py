from machine import I2C, Pin
from bmp280 import *
import utime as time
from dht import DHT11, InvalidChecksum

class Sensors:
    dhtT = 0
    dhtRh = 0
    bmpT = 0
    bmpPres = 0
    def __init__(self, bmpI2c, bmpSdaPin, bmpSclPin, dht11Pin):
        self.bmpI2c = bmpI2c
        self.bmpSdaPin = bmpSdaPin
        self.bmpSclPin = bmpSclPin
        self.dht11Pin = dht11Pin
    def BmpInit(self):
        bus = I2C(self.bmpI2c, sda=Pin(self.bmpSdaPin), scl=Pin(self.bmpSclPin)) 
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
        return self.bmp
    def DhtInit(self):
        pin = Pin(self.dht11Pin, Pin.OUT, Pin.PULL_DOWN)
        self.dht = DHT11(pin)
        return self.dht
    def getValues(self):
        dhtT = self.dht.temperature
        dhtRh = self.dht.humidity
        bmpT = self.bmp.temperature
        bmpPres = self.bmp.pressure/100

newSensors = Sensors(1, 2, 3, 28)
newSensors.BmpInit()
newSensors.DhtInit()
newSensors.getValues()
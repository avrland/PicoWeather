from machine import I2C, Pin
from bmp280 import *
import utime as time
from dht import DHT11, InvalidChecksum

def bmp_init():
    bus = I2C(0, sda=Pin(0), scl=Pin(1)) 
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
def dht_init():
    pin = Pin(28, Pin.OUT, Pin.PULL_DOWN)
    sensor = DHT11(pin)
    return sensor

bmp = bmp_init()
sensor = dht_init()
led = Pin(25, Pin.OUT)

led.value(1)
print("BMP280 Temp: " + str(bmp.temperature) + " °C")
print("BMP280 Pressure: " + str(bmp.pressure/100) + " hPa")

t  = (sensor.temperature)
h = (sensor.humidity)
print("DHT11 Temperature: {}".format(sensor.temperature) + " °C")
print("DHT11 Humidity: {}".format(sensor.humidity) + " %")
led.value(0)
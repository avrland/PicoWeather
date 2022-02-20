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
def internal_temp():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    temperature = 27 - (reading - 0.706)/0.001721
    print("Internal Pi Pico temp: " + str(temperature) + " °C")
from machine import I2C, Pin
from bmp280 import *

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


print(bmp.temperature)
print(bmp.pressure)

#True while measuring
#bmp.is_measuring

#True while copying data to registers
#bmp.is_updating
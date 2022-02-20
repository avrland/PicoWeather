from machine import I2C, Pin
from sensors import *
import utime as time

bmp_sensor = BmpInit()
dht_sensor = DhtInit()
led = Pin(25, Pin.OUT)

led.value(1)
print("BMP280 Temp: " + str(bmp_sensor.temperature) + " °C")
print("BMP280 Pressure: " + str(bmp_sensor.pressure/100) + " hPa")

print("DHT11 Temperature: {}".format(dht_sensor.temperature) + " °C")
print("DHT11 Humidity: {}".format(dht_sensor.humidity) + " %")
led.value(0)
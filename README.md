# PicoWeather
Raspberry Pi Pico Weather Station

Mix of commonly used sensors providing current weather state and temp in house also too, written in micropython. 


Wiring:

- SSD1306 (used 128x32) SDA: GP16, SCL: GP17

- BMP280 SDA: GP16, SCL: GP17

- DHT11 1wire: GP5


To start:

- upload all stuff to Pico (except main.py)
- start main.py

## Raspberry Pi Pico main.py loop stuck fix
Avoid putting main.py with loops into Pico - you'll probably get stucked and can't run REPL. If you get stucked, do this workaround:
> 1. If I plug in the pico, and then start Thonny, the printout appears in the REPL.  If I issue a STOP command, the printout stops but the pico continues to run its program.   
> 2. If I then unplug the pico, and replug it in (while Thonny is still up and running), then the pico app continues to run but produces no printout. However, I am able to stop the app using the STOP command.   
3. Save empty main.py to Pico

Source: https://forum.micropython.org/viewtopic.php?t=11147&p=61134

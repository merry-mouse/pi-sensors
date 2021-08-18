import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 17

while True:
  humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
  if humidity is not None and temperature is not None:
    print("Temp={0:.2f}C Humidity={1:.2f}%".format(temperature, humidity))
  else:
    print("NO GOOD, sensor failure. Check wiring.");
  time.sleep(1);
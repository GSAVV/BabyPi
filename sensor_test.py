import Adafruit_DHT

# Define sensor and pin data
sensor = Adafruit_DHT.DHT22
pin = 4

# Read sensor data
hum, temp = Adafruit_DHT.read_retry(sensor, pin)

# Print it
textout = 'Temperatur: ' + repr(temp) + ' und Feuchtigkeit: ' + repr(hum)
print textout

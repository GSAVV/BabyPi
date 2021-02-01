import Adafruit_DHT
import urllib2

# Define sensor and pin data
sensor = Adafruit_DHT.DHT22
pin = 4

# Read sensor data
hum, temp = Adafruit_DHT.read_retry(sensor, pin)

# Print it
textout = 'Temperatur: ' + repr(temp) + ' und Feuchtigkeit: ' + repr(hum)
print(textout)

# Send it
urlS = "http://192.168.178.50/add_data.php?temp=" + repr(temp) + "&hum="  + repr(hum)
print(urlS)
urllib2.urlopen(urlS)

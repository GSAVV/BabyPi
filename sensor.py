import Adafruit_DHT
from time import sleep
from datetime import datetime
import urllib2

def init():
	global sensor, pin, hookdir, datadir

	# Define sensor and pin data
	sensor = Adafruit_DHT.DHT22
	pin = 4

	# Define picam hook director
	hookdir = '/home/pi/picam/hooks/'

	return;

def textcreator():
	global hum, temp

	# Get Sensor data and format it
	hum, temp = Adafruit_DHT.read_retry(sensor, pin)
	try:
		temp_t = 'Temperatur: {:.1f}C '.format(temp)
		hum_t = 'Luftfeuchtigkeit: {:.1f}%'.format(hum)
	except ValueError:
		temp_t = 'no temp '
		hum_t = 'no hum'

	# Get time
	time_t = datetime.now().strftime('%H:%M')

	# Concatenate to one line
	subtitle = 'text=' +  time_t + ' Uhr ' + temp_t + hum_t

	# Write data to subtitle file
	f = open(hookdir + 'subtitle', 'w+')
	f.write(subtitle)
	f.write('\n')
	f.write('duration=115')
	f.close()

	return;

def datalogger():
	global hum, temp

	try:
		temp_t = '{:.2f}'.format(temp)
		hum_t = '{:.2f}'.format(hum)
	except ValueError:
		temp_t = '0'
		hum_t ='0'

	urlS = "http://192.168.178.50/add_data.php?temp=" + temp_t + "&hum=" + hum_t
#	print(urlS)
	urllib2.urlopen(urlS)

	return;

init()
while True:
	textcreator()
	datalogger()
	sleep(120)



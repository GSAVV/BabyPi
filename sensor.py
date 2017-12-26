import Adafruit_DHT
from time import sleep
from datetime import datetime

def init():
	global sensor, pin, hookdir, datadir

	# Define sensor and pin data
	sensor = Adafruit_DHT.DHT22
	pin = 4

	# Define picam hook director
	hookdir = '/home/pi/picam/hooks/'

	# Define data logging directiry
	datadir = '/home/pi/babylog/'

	return;

def textcreator():
	global hum, temp

	# Get Sensor data and format it
	hum, temp = Adafruit_DHT.read_retry(sensor, pin)
	temp_t = 'Temperatur: {:.1f}C '.format(temp)
	hum_t = 'Luftfeuchtigkeit: {:.1f}%'.format(hum)

	# Get time
	time_t = datetime.now().time().strftime('%H:%M')

	# Concatenate to one line
	subtitle = 'text=' +  time_t + ' Uhr ' + temp_t + hum_t

	# Write data to subtitle file
	f = open(hookdir + 'subtitle', 'w+')
	f.write(subtitle)
	f.write('\n')
	f.write('duration=57')
	f.close()

	return;

def datalogger():
	global hum, temp, datadir

	time_t = datetime.now().time().strftime('%H:%M:%S')
	temp_t = '{:.1f}%'.format(temp)
	hum_t = '{:.1f}%'.format(hum)

	f = open(datadir + 'data.csv', 'a')
	f.write(time_t + ';' + temp_t + ';' + hum_t)
	f.write('\n')
	f.close()

	return;

init()
while True:
	textcreator()
	datalogger()
	sleep(59)



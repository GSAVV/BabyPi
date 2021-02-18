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

def readsensor():
	global hum, temp

	# Get Sensor data and format it
	hum, temp = Adafruit_DHT.read_retry(sensor, pin)

def textcreator():
	global hum, temp

	# Convert readings to strings
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

def datalogger():
	import urllib.parse
	import urllib.request
	global hum, temp

	# Convert reading to string
	try:
		temp_t = '{:.2f}'.format(temp)
		hum_t = '{:.2f}'.format(hum)
	except ValueError:
		temp_t = '0'
		hum_t ='0'

	url = 'http://192.168.178.50/add_data.php'
	values = {'temp': temp_t, 
			  'hum': hum_t,
			  'name': 'sensor1'}
	data = urllib.parse.urlencode(values)
	#print(data)
	full_url = url + '?' + data
	with urllib.request.urlopen(full_url) as response:
		s = response.read()
		#print(s)

# Script execution
init()
readsensor()
#textcreator()
datalogger()

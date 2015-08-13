import sys
import time

#Custom functions
import firebase
import temphum

#Configuration
firebase_url = 'https://crackling-heat-5304.firebaseio.com'
update_interval = 60

# Parse command line parameters.
sensor_args = { '11', '22', '2302' }

if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
	sensor = sys.argv[1]
	pin = sys.argv[2]
else:
	print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
	print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
	sys.exit(1)

#Polling loop
while 1:
	newtime = time.strftime('%H:%M:%S')
	newdate = time.strftime('%d/%m/%Y')
	temperature, humidity = temphum.get(sensor, pin)
	visible, IR, uvIndex = light.get()
#	print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
	data = {'date': newdate, 'time': newtime, 'temp': '{0:0.1f}'.format(temperature), 'hum':'{0:0.1f}'.format(humidity), 'visLight':visible, 'IR':IR, 'uvIndex':uvIndex}
	print(data)
	updateRes = firebase.update(firebase_url, '/env/current.json', data)
	addRes = firebase.add(firebase_url, '/env/history.json', data)
	if(updateRes.status_code != 200):
		print(str(updateRes.status_code) + ':' + updateRes.text)
	if(addRes.status_code != 200):
		print(str(addRes.status_code) + ':' + addRes.text)
	time.sleep(update_interval)

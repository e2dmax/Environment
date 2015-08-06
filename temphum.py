import sys
import Adafruit_DHT
import requests
import time
import random
import json

firebase_url = 'https://crackling-heat-5304.firebaseio.com'

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
				'22': Adafruit_DHT.DHT22,
				'2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
	sensor = sensor_args[sys.argv[1]]
	pin = sys.argv[2]
else:
	print 'usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#'
	print 'example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4'
	sys.exit(1)

while 1:
     newtime = time.strftime('%H:%M:%S')
     newdate = time.strftime('%d/%m/%Y')

    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity is not None and temperature is not None:
    	print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
        data = {'date': newdate, 'time': newtime, 'temp': temperature, 'hum':humidity}
        result = requests.put(firebase_url + '/env.json', data=json.dumps(data))
        print(str(result.status_code) + ':' + result.text)
    else:
    	print 'Failed to get reading. Try again!'

    time.sleep(60)

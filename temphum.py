import sys
import random
#import Adafruit_DHT

def get(sensorID, pin):
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).

#	sensor_args = { '11': Adafruit_DHT.DHT11, '22': Adafruit_DHT.DHT22, '2302': Adafruit_DHT.AM2302 }
#	sensor = sensor_args[sensorID]

#	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	temperature = random.randint(6,10)*10
	humidity = random.randint(0,10)*10

	if humidity is not None and temperature is not None:
		return(temperature, humidity)
	else:
		return None

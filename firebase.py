import requests
import json

def update(url, location, data):
    try:
        result = requests.put(url + location, data=json.dumps(data))
        return result
    except:
        print('Error sending data to Firebase')
        return None

def add(url, location, data):
    try:
        result = requests.post(url + location, data=json.dumps(data))
        return result
    except:
        print('Error sending data to Firebase')
        return None

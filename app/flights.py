import json
import requests
from opensky_api import OpenSkyApi

url = "https://opensky-network.org/api/flights/departure?airport=KJFK&begin=1734696060&end=1734699660"

file = requests.get(url)

if file is not None:
    arr = json.loads(file.text)
    for i, record in enumerate(len(arr)):
        print(record.)
    

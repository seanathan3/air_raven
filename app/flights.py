import requests
from opensky_api import OpenSkyApi

url = "https://www.example.com"

file = requests.get(url)

print(file.text)


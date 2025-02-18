# import requests

# url =  "https://opensky-network.org/api/states/all?time=1458564121&icao24=3c6444"

# response = requests.get(url)

# if response.status_code == 200:
#     res = response.json()
#     print(res)

import time, math
from opensky_api import OpenSkyApi # type: ignore

current_time = math.floor(time.time())
print(current_time)

api = OpenSkyApi()
flights_over_interval = api.get_flights_from_interval(1739834916, 1739835916)
print(flights_over_interval)
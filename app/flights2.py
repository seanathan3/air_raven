# import requests

# url =  "https://opensky-network.org/api/states/all?time=1458564121&icao24=3c6444"

# response = requests.get(url)

# if response.status_code == 200:
#     res = response.json()
#     print(res)

import time, math
from opensky_api import OpenSkyApi # type: ignore

current_time = math.floor(time.time())

opensky = OpenSkyApi()
departing_flights = opensky.get_departures_by_airport("KATL", current_time - 84600, current_time)

for flight in departing_flights:
    print(flight)
    print('------')
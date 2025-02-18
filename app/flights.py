from opensky_api import OpenSkyApi
import time

api = OpenSkyApi()
s = api.get_states()
if s is not None:
    states = s.states

current_time = int(time.time())

print(states[0])

# for state in states:
#     print(current_time - state.last_contact)
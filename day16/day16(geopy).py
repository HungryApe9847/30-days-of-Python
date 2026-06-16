from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import time
geolocator = Nominatim(user_agent="my_app")
address1 = geolocator.geocode(input("Please enter an address in the UK (e.g SW1A 2AA): "))
time.sleep(1.1)
address2 = geolocator.geocode(input("Please enter another address in the UK (e.g SW1A 2AA): "))
if input("(a)km,(b)miles?").lower().strip() == "a":
    distance = geodesic((address1.latitude, address1.longitude), (address2.latitude, address2.longitude))
else:
    distance = geodesic((address1.latitude, address1.longitude), (address2.latitude, address2.longitude)).miles
print(distance)
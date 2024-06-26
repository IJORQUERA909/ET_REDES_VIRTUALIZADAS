from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="ITEM02_01")

location1 = geolocator.geocode(input("Ingresar Punto A: "))
location2 = geolocator.geocode(input("Ingresar Punto B: "))

from geopy.distance import geodesic

a = (location1.latitude,location1.longitude)
b = (location2.latitude,location2.longitude)

distancia = geodesic(a,b).km

print("la distancia entre punto A y Punto B es: ", distancia, "Km")


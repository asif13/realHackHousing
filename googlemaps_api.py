import googlemaps
from googleplaces import GooglePlaces, types



#test = "dsdwedwe";
#location_office = "tech embassy sarjapur outer ring road marathalli bangalore";
'''
api_key ="AIzaSyDraOn6uYkGmAVe01wOsd_gxyyu85TOD0w";
google_places = GooglePlaces(api_key)
gmaps = googlemaps.Client(api_key)

lat= gmaps.geocode("koramangla bangalore")
print(lat[0]['geometry']['location'])
#gmaps.local_search("hospital near" + office_location)

query_result = google_places.nearby_search(location = "koramangla bangalore",keyword='sports',
                                              radius = 20000)

for place in query_result.places:
    print(place.name)
    print(place.geo_location)
'''
api_key ="AIzaSyDraOn6uYkGmAVe01wOsd_gxyyu85TOD0w"
gmaps = googlemaps.Client(api_key)
google_places = GooglePlaces(api_key)

def get_temples(location_office):
    query_result = google_places.nearby_search(location = location_office,keyword='temple',radius = 20000)
    return query_result.places

def get_hospital(location_office):
    query_result = google_places.nearby_search(location = location_office,keyword='hospital, clinic',radius = 20000)
    return query_result.places


def get_transport(location_office):
    query_result = google_places.nearby_search(location = location_office,keyword='transport',radius = 20000)
    return query_result.places



def get_food_joints(location_office):
    query_result = google_places.nearby_search(location = location_office,keyword='food, resturants',radius = 20000)
    return query_result.places



def get_sports_center(location_office):
    query_result = google_places.nearby_search(location = location_office,keyword='sports',radius = 20000)
    return query_result.places



def get_malls(location_office):
    query_result = google_places.nearby_search(location = location_office,keyword='mall, multiplexes',radius = 20000)
    return query_result.places



def prayer_places(location_office,keyword= 'temples'):
    query_result = google_places.nearby_search(location = location_office,keyword=keyword,radius = 20000)
    return query_result.places



def girls_college(location_office):
    query_result = google_places.nearby_search(location = location_office,keyword='college',radius = 2000)
    return query_result.places


def office_location(location_office):
    lat= gmaps.geocode(location_office)
    print(lat)
    return (lat[0]['geometry']['location'])

    

'''
print(girls_college(location_office="koramangla bangalore"))
for place in girls_college(location_office = "koramangla bangalore"):
    print(place.name)
    print(place.geo_location)
'''

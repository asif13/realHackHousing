from dummmy_data import apartments_list
from building_blocks.apartments import apartments
from building_blocks.building import building
from random import randint
import googlemaps_api
import copy
from building_blocks.user import user
import json
from dummmy_data import apartment_object_list


def create_user(data):
    user_profile = json.loads(data)
    gend = 'male'
    print(user_profile['gender'])
    if user_profile['gender'] == '1':
        gend = 'female'
    new_user = user(status=user_profile['status'],sport=user_profile['sports'],gender=gend,
                    food = user_profile['veg'], office= user_profile['office'], school = user_profile['school'],
                    religion= user_profile['religion'],min_bal= user_profile['budget'][0],
                    max_bal= user_profile['budget'][1])
    return new_user

















def create_apartment_list():
    apartment_list = []
    for apartment in apartments_list:
        obj = create_apartment(apartment)
        apartment_list.append(copy.deepcopy(obj))
    
    return apartment_list
        


def create_apartment(apartment):
    address = apartment
    cost = randint(16000, 23000)
    lat , lng = googlemaps_api.office_location(apartment)
    nsp_index = calculate_nsp_index(apartment)
    transport_list = get_transport_list(apartment)
    hospital = get_hospital_list(apartment)
    obj = apartments(address = address,cost = cost,lat = lat, lng = lng,
                     nsp_index = nsp_index,transport = transport_list,hospitals = hospital)
    return obj

def get_temple_list(apartment):
    temples = googlemaps_api.prayer_places(apartment)
    temple_list = []
    for temple in temples:
        obj = building(name = temple.name, lat = temple.geo_location.lat, lng =temple.geo_location.lng)
        temple_list.append(copy.copy(obj))
    
    return temple_list

def get_transport_list(apartment):
    transports = googlemaps_api.get_transport(apartment)
    transport_list = []
    for transport in transports:
        print(transport.geo_location)
        obj = building(name = transport.name,lat = transport.geo_location.lat, lng = transport.geo_location.lng)
        transport_list.append(copy.copy(obj))
    return transport_list


def get_hospital_list(apartment):
    hospitals = googlemaps_api.get_hospital(apartment)
    hospital_list = []
    for hospital in hospitals:
        obj = building(name = hospital.name, lat = hospital.geo_location.lat,lng = hospital.geo_location.lng)
        hospital_list.append(copy.copy(obj))
    return hospital_list


def calculate_nsp_index(apartment):
    girls_colleges = googlemaps_api.girls_college(apartment)
    girl_col = 0
    if len(girls_colleges) > 5:
        girl_col = 5
    else:
        girl_col = len(girls_colleges)
    
    malls = googlemaps_api.get_malls(apartment)
    if len(malls) > 3:
        girl_col += 3
    else:
        girl_col +=len(malls)
        
    foods = googlemaps_api.get_food_joints(apartment)
    if len(foods) > 2:
        girl_col += 2
    else:
        girl_col += len(foods)
    
    print(girl_col)  
    return girl_col
    
    
    
'''    
new_apartment_list = create_apartment_list()
for apartment in new_apartment_list:
    print(apartment.address)
'''

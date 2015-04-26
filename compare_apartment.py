#from dummmy_data import apartment_object_list
from dummmy_data import apartment_object_list
import json
from building_blocks.apartments import apartments as app
'''
this is the compare apartment script
the logic is simple.
the Integlli search Engine devides the customers into two parts
1) single/ bachalor/ unmarried
2) couple/ married/ old

the first category wants a certain type of surrounding caraterized by malls, activity centers, bars,
and ofcourse NSP :p

the second Category wants nearby Hospitals, Clinics, transport, religious places, etc.

our approach is to rank the results on the basis of these parameters. 

right now the ranking is done by simple points system, but this can be further increased.

'''


apartment_list = apartment_object_list


def get_apartment_list(user):
    selected_apartment_list = []
    for apartment in apartment_list:
        var = check_apartment(apartment,user)
        if var is not None:
            selected_apartment_list.append(var)
        
    return selected_apartment_list

def check_apartment(apartment,user):
    apartment.rating = 0
    if apartment.cost < int(user.max_balance) and apartment.cost > int(user.min_balance) and _are_close_(apartment,user):
        apartment.rating += 5
        if len(apartment.public_transport) > 3:
            apartment.rating += 3
        else:
            apartment.rating -= 1
        if(user.status == 'single'):
            if len(apartment.food) > 5:
                apartment.rating += 7
            elif(len(apartment.food) < 4):
                apartment.rating -= 2
            else:
                apartment.rating += len(apartment.food)
            
            if len(user.sport) > 0:
                if len(apartment.sport) >= 2:
                    apartment.rating += 3
                else:
                    apartment.rating -= 1
            # the nsp can be directly added to the rating system
            apartment.rating += apartment.nsp_index
        
        elif(user.status == 'married'):
            if len(apartment.food) > 5:
                apartment.rating += 3
            elif len(apartment.food) < 4:
                apartment.rating -= 2
            
            if len(apartment.sport) >= 2:
                apartment.rating += 3
            else:
                apartment.rating -= 1
            
            if len(apartment.hospital) >= 1:
                apartment.rating += 3
            else:
                apartment.rating -= 2
            
            if len(apartment.public_transport) >= 1:
                apartment.rating +=2
            else:
                apartment.rating -= 1
            
        return apartment        
                
        
        
        
    else:
        return None


def _are_close_(apartment,user):
    return True



def convert_to_json(apartment_list):
    json_list = []
    for apartment in apartment_list:
        json_data = apartment.__dict__
        json_list.append(json_data)
    
    return json_list


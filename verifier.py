from data_structure.config import *


def food_verifier(food):
    if food.food_type is None or food.type_info is None:
        return False
    else:
        if (food.food_type not in food_type) or (food.type_info not in type_food):
            return False
        else:
            return True
        

def sport_verifier(obj):
    if obj is None:
        return False
    else:
        if set(obj) < set(sport):
            return True
        else:
            return False
        

    
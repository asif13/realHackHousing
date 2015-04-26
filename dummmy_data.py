from building_blocks.apartments import apartments
from random import randint
import decimal
import copy

users = [{'status':'bachelor',
          'sport':['basketball'],
          'budget_min': '5000',
          'budget_max': '15000',
          'gender':'male'},
         {'status':'bachelor',
          'sport':['basketball','cricket'],
          'budget_min': '5000',
          'budget_max': '15000',
          'gender':'female'},
         {'status':'married',
          'sport':['basketball','cricket'],
          'budget_min': '10000',
          'budget_max': '30000',
          'gender':'female'},
         ]

food = [{'type_info':'veg',
        'food_type':'North Indian'
        },
       {'type_info':'non-veg',
        'food_type':'Andra',
        },
       {'type_info':'non-veg',
        'food_type':'North Indian',
        }
        ]

region = [{'language':'Hindi',

           'religion':'Hindu'},
          {'language':'English',
           'religion':'Christian'},
          {'language':'Kannada',
           'religion':'Muslim'},
          ]


apartments_list = ['62, Forum Value Mall, Whitefield Main Road, Whitefield Prestige Ozone, Whitefield Bengaluru, Karnataka ',
        'Varthur Rd Ramagondanahalli, Whitefield Bengaluru, Karnataka 560037',
        '# 94 / 95 , 4th Cross , ECC Road , Prithvi Layout, Whitefield Bengaluru, Karnataka','Survey 5/2, Whitefield Main Road, SH 35\Sathya Sai Layout, WhitefieldBengaluru, Karnataka',
        'ECC Rd Pattandar Agrahara, Pattandur Agrahara, Whitefield Bengaluru, Karnataka',
        'Varthur Rd Ramagondanahalli, Whitefield Bengaluru, Karnataka ',
        '6th Cross, Holy Cross school Road Happy Valley, Whitefield Bengaluru, Karnataka',
        'Borewell Road Whitefield Palm Meadows, Whitefield Bengaluru, Karnataka',
        'SH 35 Narayanappa Garden, Whitefield Bengaluru, Karnataka',
        'No.35/5C, Varthur Main Road, Whitefield Ramagondanahalli, Whitefield Bengaluru, Karnataka',
        'ITPL Main Rd BEML Layout, Brookefield Bengaluru, Karnataka',
        '600, 2nd Floor, C Block AECS Layout, Infront of M.K.Retail AECS Layout - C Block, AECS Layout, Brookefield Bengaluru, Karnataka',
        'A- 403 , Knights Bridge Apts, Brooke fields Kundalahalli , Whitefields Bengaluru, Karnataka'
        ]

def calculate_nsp_index(apartment):
    score = 0
    if len(apartment.college) >=1:
        score += 5
    else:
        pass
    if len(apartment.malls) >= 2:
        score += 3
    else:
        score += 0
        
    if len(apartment.food) > 2:
        score += 2
    else:
        score += 0
    
    apartment.nsp_index = score 



apartment_object_list =[] 

address = apartments_list[0]
cost = randint(16000,21000)
lat = "12.9566294"
lng = "77.70468230000006"
public_transport = ['Bus Stop1', 'Bus Stop2', 'Bus Stop3']
hospital = ['hospital1', 'Hospital2','Hospital3']
food = ['Food1','Food2','Food3','Foood4','Food5','Food6']
sport = ['Sport1','Sport2','Sport3']
malls = ['mall1','Mall2','Mall3']
college = ['College1','College2','College3']

apartment1 = apartments(address=address,cost = cost,lat = lat, lng = lng, transport = public_transport,
                        hospitals=hospital,food=food,sport=sport,mall=malls,college=college,nsp_index= 0)

calculate_nsp_index(apartment1)
apartment_object_list.append(copy.copy(apartment1))   

address = apartments_list[1]
cost = randint(16000,21000)
lat = "12.9666294"
lng = "77.71468230000006"
public_transport = ['Bus Stop1', 'Bus Stop2', 'Bus Stop3']
hospital = ['hospital1', 'Hospital2','Hospital3']
food = ['Food1','Food3','Foood4','Food5','Food6']
sport = []
malls = ['mall1','Mall2']
college = ['College1','College2','College3']

apartment2 = apartments(address=address,cost = cost,lat = lat, lng = lng, transport = public_transport,
                        hospitals=hospital,food=food,sport=sport,mall=malls,college=college,nsp_index= 0)

calculate_nsp_index(apartment2)
apartment_object_list.append(copy.copy(apartment2))   
    
    
address = apartments_list[2]
cost = randint(16000,21000)
lat = "12.9066294"
lng = "77.69468230000006"
public_transport = ['Bus Stop1', 'Bus Stop2', 'Bus Stop3','Bus Stop4']
hospital = []
food = ['Food1','Food2','Food3','Foood4','Food5','Food6']
sport = ['Sport1','Sport2','Sport3']
malls = ['mall1','Mall2','Mall3','mall4','mall5','mall6']
college = ['College1','College2','College3']

apartment3 = apartments(address=address,cost = cost,lat = lat, lng = lng, transport = public_transport,
                        hospitals=hospital,food=food,sport=sport,mall=malls,college=college,nsp_index= 0)

calculate_nsp_index(apartment3)
apartment_object_list.append(copy.copy(apartment3))   


address = apartments_list[3]
cost = randint(16000,21000)
lat = "12.9366294"
lng = "77.73468230000006"
public_transport = ['Bus Stop1', 'Bus Stop2', 'Bus Stop3']
hospital = ['hospital1', 'Hospital2','Hospital3']
food = ['Food1','Food2','Food3','Food5','Food6']
sport = ['Sport1','Sport2','Sport3']
malls = ['mall1','Mall2','Mall3']
college = ['College1','College2','College3']

apartment4 = apartments(address=address,cost = cost,lat = lat, lng = lng, transport = public_transport,
                        hospitals=hospital,food=food,sport=sport,mall=malls,college=college,nsp_index= 0)

calculate_nsp_index(apartment4)
apartment_object_list.append(copy.copy(apartment4))   


address = apartments_list[4]
cost = randint(16000,21000)
lat = "12.9400294"
lng = "77.71408230000006"
public_transport = ['Bus Stop1', 'Bus Stop2', 'Bus Stop3']
hospital = ['hospital1', 'Hospital2','Hospital3']
food = ['Food1','Food2','Food3','Foood4','Food5','Food6']
sport = ['Sport1','Sport2','Sport3']
malls = []
college = []

apartment5 = apartments(address=address,cost = cost,lat = lat, lng = lng, transport = public_transport,
                        hospitals=hospital,food=food,sport=sport,mall=malls,college=college,nsp_index= 0)

calculate_nsp_index(apartment5)
apartment_object_list.append(copy.copy(apartment5))   



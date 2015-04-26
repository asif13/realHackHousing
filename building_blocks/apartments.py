
class apartments(object):
    def __init__(self, address, cost, lat, lng,nsp_index, transport, hospitals,food,sport,mall,
                 college):
        self.address = address
        self.cost = cost
        self.lat = lat
        self.lng = lng
        self.nsp_index = nsp_index
        self.public_transport = transport # list of Transport
        self.hospital = hospitals # list of buildings
        self.rating = 0
        self.food = food
        self.sport = sport
        self.malls = mall
        self.college = college
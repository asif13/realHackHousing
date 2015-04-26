from flask import Flask,request
from helper import create_user
from compare_apartment import get_apartment_list
from compare_apartment import convert_to_json
import json

class Orchestrator(object):
    def __init__(self):
        self.user = None
    
    
    def handle_user(self,user):
        self.user = create_user(user)
        apartment_list = get_apartment_list(self.user)
        json_data = convert_to_json(apartment_list)
        #print(self.user.gender)
        for apart in apartment_list:
            print(apart.address)
        #print(apartment_list[0].address)
        return json.dumps(json_data)

orchestrator = Orchestrator()

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/user',methods = ['POST'])
def user():
    json_data = request.get_data()
    print(json_data)
    output = orchestrator.handle_user(json_data)
    return output


if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug = True)
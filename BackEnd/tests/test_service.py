import requests
import json

url = 'http://127.0.0.1:5000/open'
# r = requests.get(url)
# print("status_code:", r.status_code)
# print("status_code:", r.text)

# myobj = {'api_call': '2021:06:30:19:05'}
# data_json = json.dumps(myobj)
# x = requests.post(url, json=data_json)
#
# print(x.text)



def test_server_is_up():
    r = requests.get(url)
    assert(200 == r.status_code)
    assert("This is not the page you are looking for." == json.loads(r.text)['message'])

def test_server_app_call():
    myobj = {'api_call': '2021:06:30:19:05'}
    data_json = json.dumps(myobj)
    x = requests.post(url, json=data_json)
    d = json.loads(x.text)
    assert(d == {'open': ['The Cowfish Sushi Burger Bar', 'Morgan St Food Hall', 'Garland', 'Crawford and Son', 'Bida Manda', 'The Cheesecake Factory', 'Tupelo Honey', "Player's Retreat", 'Glenwood Grill', 'Neomonde', 'Page Road Grill', 'Mez Mexican', 'Saltbox', 'El Rodeo', 'Provence', 'Tazza Kitchen', 'Mandolin', "Mami Nora's", 'Gravy', 'Taverna Agora', 'Char Grill', 'Whiskey Kitchen', 'Sitti', 'Yard House', "David's Dumpling", 'Gringo a Gogo', 'Centro', 'Brewery Bhavana', 'Dashi', 'Top of the Hill', 'Jose and Sons', 'Oakleaf', 'Second Empire']})

import requests
import json

response = requests.get('https://randomuser.me/api/?resutls=10')

data = response.json()

for user in data['results']:
    print(user['name']['first'])

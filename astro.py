import requests

response = requests.get('http://api.open-notify.org/astros.json')

print(response.status_code)
data = response.json()
astronauts = data.get('people', [])

for astronaut in astronauts[:5]:
    print(astronaut['name'])
import requests
userdata = "suffering"


myobj = {'text': userdata}
url = 'http://text-processing.com/api/sentiment/'
response = requests.post(url, data=myobj)

if response.status_code == 200:
  print(response.json())
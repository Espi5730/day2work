# WRITE YOUR CODE HERE
import requests

url = 'https://httpbin.org/post'
response = requests.post(url)

if response.status_code == 200:
  print(response.json())


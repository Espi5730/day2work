import requests
import json

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
response = requests.get(url)
     
# check request
if response.status_code == 200:
  data = response.json()
  last_refreshed = data["Meta Data"]["3. Last Refreshed"]
  price = data["Time Series (5min)"][last_refreshed]["1. open"]

print(data)
import requests
import json
import pandas as pd
import sqlalchemy as db

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
response = requests.get(url)

engine = db.create_engine('sqlite:///stockdata.db')

# check request
if response.status_code == 200:
    data = response.json()
    timedata = data.get('Time Series (5min)', {})
    newdict = pd.DataFrame.from_dict(timedata, orient='index')
    newdict.reset_index(inplace=True)
    # rename columns
    newdict.rename(columns={
        'index': 'datetime',
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    }, inplace=True)

    newdict['datetime'] = pd.to_datetime(newdict['datetime'])
    newdict.to_sql('Stock_Data', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
    query_result = connection.execute(db.text("SELECT * FROM Stock_Data;")).fetchall()
    print(pd.DataFrame(query_result))
# Stock Data Fetcher

This project fetches stock data for IBM from an API, stores it in a database, and then queries and displays the  data.

## Setup Instructions

run pip install requests pandas sqlalchemy in a terminal
then use python3 code.py

### How the code works
the code follows the following steps
- Fetches data from API
- Converts JSON response into dataframe
- stores into SQL 
- Prints the data via a Query
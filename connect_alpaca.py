import alpaca_trade_api as tradeapi
import pandas as pd
from polygon import RESTClient

# Alpaca API keys
API_KEY = "PK5C0C654P8X45H5F2VK"
SECRET_KEY = "pqWr0dk8q2x6oq45jZ9SxGDdpS9CcW6h5UjYAtvL"
BASE_URL = "https://paper-api.alpaca.markets"  # Use this for paper trading

# Polygon API key
client = RESTClient(api_key="3lg6jdDXLUEyxwQde0YrOfPUpY0_nIg0")

# Create an API connection
api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

# Fetch account details
account = api.get_account()

# Print account status
print(f"Account Status: {account.status}")
print(f"Buying Power: ${account.buying_power}")

# Get stock data
ticker = "AAPL"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
    aggs.append(a)

print(aggs)

# Get Last Trade
trade = client.get_last_trade(ticker=ticker)
print(trade)

# List Trades
trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
for trade in trades:
    print(trade)

# Get Last Quote
quote = client.get_last_quote(ticker=ticker)
print(quote)

# List Quotes
quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
for quote in quotes:
    print(quote)
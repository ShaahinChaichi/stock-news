import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
ACCESS_KEY = "MO5LQIYP48RPIBR5"

# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=demo

params = {"function": "TIME_SERIES_DAILY_ADJUSTED",
          "symbol": "IBM",
          "apikey": ACCESS_KEY,
          }

response = requests.get(STOCK_ENDPOINT, params=params)
data = response.json()

yesterday_closing_price = []
before_yesterday_closing_price = []

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday
# then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g.
#  [new_value for (key, value) in dictionary.items()]
time_series_price = data['Time Series (Daily)']

for day, price in time_series_price.items():
    if day == "2023-06-15":
        closing_price = price['4. close']
        yesterday_closing_price = closing_price
    if day == "2023-06-14":
        closing_price = price['4. close']
        before_yesterday_closing_price = closing_price

# TODO 2. - Get the day before yesterday's closing stock price
print(yesterday_closing_price)
print(before_yesterday_closing_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20.
#  Hint: https://www.w3schools.com/python/ref_func_abs.asp

# TODO 4. - Work out the percentage difference in price between closing price yesterday and
#  closing price the day before yesterday.

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
